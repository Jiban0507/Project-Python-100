from flask import session

from app.models import Product

CART_KEY = "cart"  # session[CART_KEY] = { product_id: quantity }


def get_cart_dict():
    return session.get(CART_KEY, {})


def save_cart_dict(cart):
    session[CART_KEY] = cart
    session.modified = True


def add_item(product_id, quantity=1):
    cart = get_cart_dict()
    cart[product_id] = cart.get(product_id, 0) + quantity
    save_cart_dict(cart)


def update_item(product_id, quantity):
    cart = get_cart_dict()
    if quantity < 1:
        cart.pop(product_id, None)
    else:
        cart[product_id] = quantity
    save_cart_dict(cart)


def remove_item(product_id):
    cart = get_cart_dict()
    cart.pop(product_id, None)
    save_cart_dict(cart)


def clear_cart():
    session.pop(CART_KEY, None)


def get_cart_items():
    """Resolve the session's {product_id: qty} into a list of (product, quantity)."""
    cart = get_cart_dict()
    if not cart:
        return []

    products = Product.query.filter(Product.id.in_(cart.keys())).all()
    products_by_id = {p.id: p for p in products}

    items = []
    for product_id, quantity in cart.items():
        product = products_by_id.get(product_id)
        if product:  # skip items for products that no longer exist
            items.append((product, quantity))
    return items


def get_cart_total():
    return sum(product.price * quantity for product, quantity in get_cart_items())


def get_cart_count():
    return sum(get_cart_dict().values())
