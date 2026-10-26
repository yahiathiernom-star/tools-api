from flask import jsonify


def erreur_400(message="Paramètres invalides"):
    return jsonify({
        "erreur": message,
        "code": 400
    }), 400