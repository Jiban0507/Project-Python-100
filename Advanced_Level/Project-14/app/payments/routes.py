import stripe
from flask import current_app, render_template, request, redirect, url_for, flash, jsonify  # noqa: F401
from flask_login import login_required, current_user

from app.payments import payments_bp
from app.extensions import db
from app.models import Order, OrderItem, Product
from app.cart import utils as cart_utils


@payments_bp.route("/checkout", methods=["POST"])
@login_required
def checkout():
    stripe.api_key = current_app.config["STRIPE_SECRET_KEY"]

    cart_items = cart_utils.get_cart_items()  # [(product, quantity), ...]
    if not cart_items:
        flash("Your cart is empty.", "error")
        return redirect(url_for("cart.view_cart"))

    # Always trust server-side prices/stock, never anything from the client.
    line_items = []
    total = 0.0
    order_items_data = []

    for product, quantity in cart_items:
        fresh_product = db.session.get(Product, product.id)
        if not fresh_product:
            flash(f"{product.name} is no longer available.", "error")
            return redirect(url_for("cart.view_cart"))
        if fresh_product.stock < quantity:
            flash(f"Not enough stock for {fresh_product.name}.", "error")
            return redirect(url_for("cart.view_cart"))

        total += fresh_product.price * quantity
        order_items_data.append(
            dict(product_id=fresh_product.id, name=fresh_product.name, quantity=quantity, price=fresh_product.price)
        )
        line_items.append(
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": fresh_product.name,
                        "images": [fresh_product.image_url] if fresh_product.image_url else [],
                    },
                    "unit_amount": round(fresh_product.price * 100),  # Stripe expects cents
                },
                "quantity": quantity,
            }
        )

    order = Order(user_id=current_user.id, status="pending", total=total)
    db.session.add(order)
    db.session.flush()  # get order.id before commit

    for item_data in order_items_data:
        db.session.add(OrderItem(order_id=order.id, **item_data))
    db.session.commit()

    try:
        checkout_session = stripe.checkout.Session.create(
            mode="payment",
            payment_method_types=["card"],
            line_items=line_items,
            success_url=current_app.config["BASE_URL"] + url_for("payments.order_success", order_id=order.id),
            cancel_url=current_app.config["BASE_URL"] + url_for("cart.view_cart"),
            metadata={"order_id": order.id, "user_id": current_user.id},
        )
    except Exception as e:
        current_app.logger.error(f"Stripe checkout session creation failed: {e}")
        flash("Something went wrong starting checkout. Please try again.", "error")
        return redirect(url_for("cart.view_cart"))

    order.stripe_session_id = checkout_session.id
    db.session.commit()

    return redirect(checkout_session.url, code=303)


@payments_bp.route("/order-success/<order_id>")
@login_required
def order_success(order_id):
    order = Order.query.filter_by(id=order_id, user_id=current_user.id).first_or_404()
    cart_utils.clear_cart()  # payment flow completed — safe to empty the cart
    return render_template("order_success.html", order=order)


@payments_bp.route("/webhook/stripe", methods=["POST"])
def stripe_webhook():
    stripe.api_key = current_app.config["STRIPE_SECRET_KEY"]
    payload = request.get_data()
    sig_header = request.headers.get("Stripe-Signature")

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, current_app.config["STRIPE_WEBHOOK_SECRET"])
    except (ValueError, stripe.error.SignatureVerificationError) as e:
        current_app.logger.error(f"Webhook signature verification failed: {e}")
        return jsonify({"error": "invalid signature"}), 400

    if event["type"] == "checkout.session.completed":
        session_obj = event["data"]["object"]
        order_id = session_obj.get("metadata", {}).get("order_id")

        if order_id:
            order = db.session.get(Order, order_id)
            if order and order.status != "paid":
                order.status = "paid"
                for item in order.items:
                    product = db.session.get(Product, item.product_id)
                    if product:
                        product.stock = max(0, product.stock - item.quantity)
                db.session.commit()
                current_app.logger.info(f"Order {order_id} marked as paid.")

    return jsonify({"received": True})
