from flask import Blueprint, request, jsonify

from app.erreurs import erreur_400

math_bp = Blueprint("math", __name__)


@math_bp.get("/factorielle")
def factorielle():
    n = request.args.get("n")

    # Vérifier que le paramètre existe
    if n is None:
        return erreur_400("Le paramètre n est obligatoire")

    # Vérifier que n est un entier
    try:
        n = int(n)
    except ValueError:
        return erreur_400("Le paramètre n doit être un entier")

    # Une factorielle n'accepte pas les nombres négatifs
    if n < 0:
        return erreur_400("Le paramètre n doit être positif ou nul")

    # Calculer la factorielle
    resultat = 1
    for i in range(2, n + 1):
        resultat *= i

    return jsonify({"resultat": resultat}), 200


@math_bp.get("/est_premier")
def est_premier():
    n = request.args.get("n")

    if n is None:
        return erreur_400("Le paramètre n est obligatoire")

    try:
        n = int(n)
    except ValueError:
        return erreur_400("Le paramètre n doit être un entier")

    if n < 2:
        return jsonify({"resultat": False}), 200

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return jsonify({"resultat": False}), 200

    return jsonify({"resultat": True}), 200