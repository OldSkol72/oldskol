from flask import Flask, jsonify
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Retrieve API Key from environment variables
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

@app.route('/get-api-key')
def get_api_key():
    """Return the Google Maps API key securely."""
    if not API_KEY:
        return jsonify({"error": "API key not found"}), 500
    return jsonify({"apiKey": API_KEY})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
