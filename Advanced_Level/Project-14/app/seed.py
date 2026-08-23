from app.extensions import db
from app.models import Product

SAMPLE_PRODUCTS = [
    dict(name="Wireless Headphones", description="Over-ear, noise-cancelling, 30h battery life.",
         price=79.99, image_url="https://picsum.photos/seed/headphones/400/400", category="Electronics", stock=25),
    dict(name="Mechanical Keyboard", description="Hot-swappable switches, RGB backlight.",
         price=129.99, image_url="https://picsum.photos/seed/keyboard/400/400", category="Electronics", stock=15),
    dict(name="Ceramic Coffee Mug", description="350ml, dishwasher safe, minimalist design.",
         price=14.50, image_url="https://picsum.photos/seed/mug/400/400", category="Home", stock=100),
    dict(name="Canvas Backpack", description="Water-resistant, padded laptop sleeve.",
         price=54.00, image_url="https://picsum.photos/seed/backpack/400/400", category="Accessories", stock=40),
    dict(name="Desk Lamp", description="Adjustable LED lamp with 3 brightness levels.",
         price=32.99, image_url="https://picsum.photos/seed/lamp/400/400", category="Home", stock=60),
    dict(name="Running Shoes", description="Lightweight breathable mesh, cushioned sole.",
         price=89.00, image_url="https://picsum.photos/seed/shoes/400/400", category="Apparel", stock=30),
    dict(name="Stainless Water Bottle", description="Keeps drinks cold for 24h, 750ml.",
         price=22.00, image_url="https://picsum.photos/seed/bottle/400/400", category="Accessories", stock=80),
    dict(name="Bluetooth Speaker", description="Portable, IPX7 waterproof, 12h playback.",
         price=45.99, image_url="https://picsum.photos/seed/speaker/400/400", category="Electronics", stock=20),
]


def seed_products():
    if Product.query.count() > 0:
        return
    for data in SAMPLE_PRODUCTS:
        db.session.add(Product(**data))
    db.session.commit()
    print(f"Seeded {len(SAMPLE_PRODUCTS)} products.")
