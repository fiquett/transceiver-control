from functools import wraps
from flask import request, jsonify
import os

# Load the secret token from an environment variable
SECRET_TOKEN = os.getenv("SECRET_TOKEN", "default_secret")

def token_required(f):
    """
    Decorator to require an authentication token for Flask routes.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token or token.split()[1] != SECRET_TOKEN:
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated
