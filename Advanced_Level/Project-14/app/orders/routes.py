from flask import render_template, abort
from flask_login import login_required, current_user

from app.orders import orders_bp
from app.models import Order


@orders_bp.route("/")
@login_required
def list_orders():
    orders = (
        Order.query.filter_by(user_id=current_user.id)
        .order_by(Order.created_at.desc())
        .all()
    )
    return render_template("orders.html", orders=orders)


@orders_bp.route("/<order_id>")
@login_required
def detail(order_id):
    order = Order.query.filter_by(id=order_id, user_id=current_user.id).first()
    if not order:
        abort(404)
    return render_template("order_detail.html", order=order)
