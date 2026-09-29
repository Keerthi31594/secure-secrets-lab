import os
import requests

API_KEY = os.environ["PAYMENTS_API_KEY"]

def charge(amount_cents: int):
    return requests.post(
        "https://api.example-payments.test/v1/charges",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={"amount": amount_cents, "currency": "usd"},
        timeout=5,
    )
