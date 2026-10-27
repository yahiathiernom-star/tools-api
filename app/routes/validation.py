import re

from flask import Blueprint, jsonify, request

from app.erreurs import erreur_400

validation_bp = Blueprint("validation", __name__)

EMAIL_REGEX = re.compile(r"^[\w.+-]+@[\w-]+\.[\w.-]+$")


@validation_bp.get("/email_valide")
def email_valide():
    email = request.args.get("email", "").strip()

    if not email:
        return erreur_400("Le paramètre 'email' est requis")

    return jsonify({"email": email, "valide": bool(EMAIL_REGEX.match(email))}), 200