import os
from flask import Flask, jsonify
from flask_cors import CORS

# Load .env variables only in local development
debug_mode = os.getenv("RENDER") is None
if debug_mode:
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ModuleNotFoundError:
        print("Warning: dotenv module not found. Skipping local environment loading.")

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to the Oldskol API"

@app.route('/get-api-key')
def get_api_key():
    api_key = os.getenv("GOOGLE_MAPS_API_KEY", "Key_Not_Found")
    return jsonify({"apiKey": api_key})  # Returns the secure key

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Use Render's provided PORT
    app.run(host='0.0.0.0', port=port)

