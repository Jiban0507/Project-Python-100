# 🛍️ E-commerce Platform (Python)

> Full-stack online store — Flask, SQLAlchemy, Jinja2, Stripe payment integration

[![License](https://img.shields.io/badge/License-AGPL--3.0-e8b84b?style=flat-square)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=flat-square&logo=flask)
![Stripe](https://img.shields.io/badge/Stripe-Checkout-635BFF?style=flat-square&logo=stripe)
![SQLite](https://img.shields.io/badge/SQLite-SQLAlchemy-003B57?style=flat-square&logo=sqlite)

A single Python web app — Flask serves both the API logic and the HTML (via Jinja2 templates), so there's no separate frontend build step. This is a from-scratch Python rewrite of the same project's Node/React version, built to the same requirements: full-stack, payment integration, database.

---

## 🚀 Features

- **Product catalog** — browse, search by keyword, and filter by category
- **Authentication** — Flask-Login session auth, passwords hashed with Werkzeug's `generate_password_hash`
- **Cart** — stored server-side in the Flask session (no JS framework needed), quantity editing, live totals
- **Stripe Checkout integration** — real payment flow using Stripe's hosted Checkout page (test mode)
- **Server-trusted pricing** — the backend re-fetches each product's real price/stock from the database at checkout time; it never trusts anything submitted by the client
- **Webhook-driven order confirmation** — orders flip from `pending` → `paid` only once Stripe confirms payment via a signature-verified webhook, and stock is decremented at that point
- **Order history** — logged-in users can view past orders and their status
- **SQLite + SQLAlchemy** — zero-config relational storage, auto-seeded with sample products on first run
- **Protected routes** — order history and checkout require login; both redirect to the login page otherwise

---

## 📁 Project Structure

```
ecommerce-platform-python/
├── run.py                     # entry point — python run.py
├── requirements.txt
├── .env.example
└── app/
    ├── __init__.py             # app factory — creates & configures the Flask app
    ├── extensions.py           # db (SQLAlchemy) + login_manager instances
    ├── models.py                # User, Product, Order, OrderItem
    ├── seed.py                  # sample product seed data
    ├── auth/
    │   └── routes.py             # register / login / logout
    ├── products/
    │   └── routes.py             # product listing + detail
    ├── cart/
    │   ├── utils.py               # session-based cart helpers
    │   └── routes.py              # add / update / remove / view cart
    ├── orders/
    │   └── routes.py             # order history (login required)
    ├── payments/
    │   └── routes.py             # Stripe Checkout session + webhook handler
    ├── templates/                # Jinja2 templates (server-rendered HTML)
    │   ├── base.html               # nav, flash messages, layout
    │   ├── home.html, product_detail.html
    │   ├── cart.html
    │   ├── login.html, register.html
    │   ├── orders.html, order_detail.html, order_success.html
    └── static/css/style.css      # single stylesheet, no build step
```

---

## ⚙️ Setup

### 1. Get a free Stripe test account
Sign up at [stripe.com](https://dashboard.stripe.com/register) — no business verification needed for **test mode**. Grab your test **Secret key** from [dashboard.stripe.com/test/apikeys](https://dashboard.stripe.com/test/apikeys).

### 2. Install and configure

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
cp .env.example .env
# edit .env — paste in your Stripe test secret key (STRIPE_SECRET_KEY)
# and set FLASK_SECRET_KEY to a long random string
```

### 3. Run it

```bash
python run.py
```

Visit `http://localhost:5000`. The database and sample products are created automatically on first run — no migration step needed.

### 4. Forward Stripe webhooks to your local server
Stripe needs to reach your webhook endpoint to confirm payments. Use the [Stripe CLI](https://docs.stripe.com/stripe-cli):

```bash
stripe login
stripe listen --forward-to localhost:5000/webhook/stripe
```

This prints a webhook signing secret (`whsec_...`) — put that in `.env` as `STRIPE_WEBHOOK_SECRET`, then restart the app.

---

## ▶️ Usage

1. **Sign up** for an account (or log in)
2. **Browse products**, use search/category filters, add items to your cart
3. Go to **Cart** and click **Checkout with Stripe** — you're redirected to Stripe's hosted Checkout page
4. Use a [Stripe test card](https://docs.stripe.com/testing#cards) — e.g. `4242 4242 4242 4242`, any future expiry, any CVC
5. On success, you land on the order confirmation page; once the webhook fires (usually within a second or two), the order's status flips to **paid** and product stock is decremented
6. Check **My Orders** to see order history and status

### Key settings (`.env`)

| Variable                | Description                                                        |
|---------------------------|--------------------------------------------------------------------|
| `FLASK_SECRET_KEY`         | Secret used to sign session cookies — use a long random string       |
| `BASE_URL`                 | Base URL used to build Stripe's success/cancel redirect URLs         |
| `DATABASE_URL`             | SQLAlchemy database URI (defaults to a local SQLite file)            |
| `STRIPE_SECRET_KEY`        | Your Stripe **test** secret key                                       |
| `STRIPE_WEBHOOK_SECRET`    | Signing secret from `stripe listen` (or your Dashboard webhook config) |

---

## 🔒 Security notes

- Passwords are hashed with Werkzeug's PBKDF2-based hasher before storage — plaintext passwords are never stored or logged
- Flask-Login handles session auth; `@login_required` protects checkout and order routes, redirecting anonymous users to login
- **Prices are never trusted from the client** — the checkout route re-fetches each product's real price and stock from the database before building the Stripe session
- The Stripe webhook signature is verified using the raw request body (`stripe.Webhook.construct_event`), so only genuine events from Stripe can mark an order as paid
- This is a learning/portfolio project, not an audited production system — before shipping something like this for real, add CSRF protection (e.g. Flask-WTF), rate limiting, stricter input validation, HTTPS enforcement, and a proper secrets-management setup

---

## 🧪 Verifying it works

Every route in this app was exercised with Flask's `test_client` during development — registration (including duplicate-email rejection), login/logout, product browsing, add/update/remove cart, checkout auth guards, and order history all pass. No separate test suite ships with the project, but the same pattern (`app.test_client()`, no real server needed) is a good starting point if you want to add one.

---

## 📄 License

AGPL-3.0 License — see [LICENSE](LICENSE)
