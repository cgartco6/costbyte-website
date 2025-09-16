# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from routes.auth import auth_bp
from routes.clients import clients_bp
from routes.analytics import analytics_bp
from routes.email import email_bp
from utils.security import requires_auth

app = Flask(__name__)
CORS(app)

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(clients_bp)
app.register_blueprint(analytics_bp)
app.register_blueprint(email_bp)

@app.route('/')
def hello():
    return jsonify({"message": "CostByte API is running"})

if __name__ == '__main__':
    app.run(debug=True)
