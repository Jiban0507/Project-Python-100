from flask import render_template, request, redirect, url_for, flash

from app.cart import cart_bp
from app.cart import utils as cart_utils
from app.models import Product


@cart_bp.route("/")
def view_cart():
    items = cart_utils.get_cart_items()
    total = cart_utils.get_cart_total()
    return render_template("cart.html", items=items, total=total)


@cart_bp.route("/add/<product_id>", methods=["POST"])
def add(product_id):
    product = Product.query.get(product_id)
    if not product:
        flash("Product not found.", "error")
        return redirect(url_for("products.home"))

    quantity = max(1, int(request.form.get("quantity", 1)))
    cart_utils.add_item(product_id, quantity)
    flash(f"Added {product.name} to your cart.", "success")
    return redirect(request.referrer or url_for("products.home"))


@cart_bp.route("/update/<product_id>", methods=["POST"])
def update(product_id):
    quantity = int(request.form.get("quantity", 1))
    cart_utils.update_item(product_id, quantity)
    return redirect(url_for("cart.view_cart"))


@cart_bp.route("/remove/<product_id>", methods=["POST"])
def remove(product_id):
    cart_utils.remove_item(product_id)
    return redirect(url_for("cart.view_cart"))
