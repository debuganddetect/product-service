"""product-service — simple products API for DevOps learning."""

from flask import Flask, jsonify

app = Flask(__name__)

PRODUCTS = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 79999,
        "currency": "INR",
        "category": "electronics",
        "in_stock": True,
    },
    {
        "id": 2,
        "name": "Wireless Mouse",
        "price": 1299,
        "currency": "INR",
        "category": "electronics",
        "in_stock": True,
    },
    {
        "id": 3,
        "name": "Notebook",
        "price": 149,
        "currency": "INR",
        "category": "stationery",
        "in_stock": False,
    },
]


@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": "product-service"}), 200


@app.get("/products")
def get_products():
    """Return a hardcoded list of products as application/json."""
    return jsonify(PRODUCTS), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
