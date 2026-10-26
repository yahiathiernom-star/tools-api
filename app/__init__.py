from flask import Flask, jsonify

from app.routes.math import math_bp
from app.routes.texte import texte_bp
from app.routes.conversion import conversion_bp
from app.routes.validation import validation_bp


def create_app():
    app = Flask(__name__)

    # Enregistrement des modules
    app.register_blueprint(math_bp, url_prefix="/math")
    app.register_blueprint(texte_bp, url_prefix="/texte")
    app.register_blueprint(conversion_bp, url_prefix="/conversion")
    app.register_blueprint(validation_bp, url_prefix="/validation")

    # Route commune : état de l'API
    @app.get("/sante")
    def sante():
        return jsonify({"status": "ok"}), 200

    return app