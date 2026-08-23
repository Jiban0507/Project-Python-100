from flask import render_template, request, abort

from app.products import products_bp
from app.models import Product


@products_bp.route("/")
def home():
    search = request.args.get("search", "").strip()
    category = request.args.get("category", "").strip()

    query = Product.query
    if search:
        like = f"%{search}%"
        query = query.filter(Product.name.ilike(like) | Product.description.ilike(like))
    if category:
        query = query.filter_by(category=category)

    products = query.order_by(Product.created_at.desc()).all()
    categories = sorted({p.category for p in Product.query.all() if p.category})

    return render_template(
        "home.html", products=products, categories=categories, search=search, category=category
    )


@products_bp.route("/products/<product_id>")
def detail(product_id):
    product = Product.query.get(product_id)
    if not product:
        abort(404)
    return render_template("product_detail.html", product=product)
