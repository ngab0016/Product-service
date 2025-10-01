from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Health check / root route
@app.route('/')
def home():
    return "✅ Flask app is running on Azure App Service!"

# Products endpoint
@app.route('/products', methods=['GET'])
def get_products():
    products = [
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99}
    ]
    return jsonify(products)

if __name__ == '__main__':
    # Azure provides PORT dynamically, fall back to 3030 if missing
    port = int(os.getenv("PORT", 3030))
    app.run(host="0.0.0.0", port=port)
