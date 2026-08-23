from flask import Blueprint

orders_bp = Blueprint("orders", __name__, url_prefix="/orders")

from app.orders import routes  # noqa: E402,F401
