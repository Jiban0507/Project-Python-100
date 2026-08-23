import os

from flask import Flask
from dotenv import load_dotenv

from app.extensions import db, login_manager

load_dotenv()


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY", "dev-only-change-me")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///store.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["BASE_URL"] = os.environ.get("BASE_URL", "http://localhost:5000")
    app.config["STRIPE_SECRET_KEY"] = os.environ.get("STRIPE_SECRET_KEY", "")
    app.config["STRIPE_WEBHOOK_SECRET"] = os.environ.get("STRIPE_WEBHOOK_SECRET", "")

    db.init_app(app)
    login_manager.init_app(app)

    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, user_id)

    from app.auth.routes import auth_bp
    from app.products.routes import products_bp
    from app.cart.routes import cart_bp
    from app.orders.routes import orders_bp
    from app.payments.routes import payments_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(orders_bp)
    app.register_blueprint(payments_bp)

    from app.cart.utils import get_cart_count

    @app.context_processor
    def inject_cart_count():
        return {"cart_count": get_cart_count}

    with app.app_context():
        db.create_all()
        from app.seed import seed_products
        seed_products()

    return app
