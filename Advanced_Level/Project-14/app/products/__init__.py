from flask import Blueprint

products_bp = Blueprint("products", __name__)

from app.products import routes  # noqa: E402,F401
