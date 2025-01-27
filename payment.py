import stripe
from flask import Blueprint, request

payment_routes = Blueprint("payment_routes", __name__)
stripe.api_key = "your_stripe_secret_key"

@payment_routes.route('/api/checkout', methods=['POST'])
def checkout():
    data = request.json
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": "usd",
                "product_data": {"name": "AI Tutoring Premium Access"},
                "unit_amount": 1000  # Amount in cents
            },
            "quantity": 1
        }],
        mode="payment",
        success_url="https://your-frontend-url/success",
        cancel_url="https://your-frontend-url/cancel",
    )
    return {"url": session.url}, 200
