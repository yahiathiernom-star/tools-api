from flask import Blueprint, jsonify, request

from app.erreurs import erreur_400

texte_bp = Blueprint("texte", __name__)

VOYELLES = "aeiouyàâäéèêëîïôöùûü"


def _verifier(texte):
    if not isinstance(texte, str):
        raise ValueError("Le texte doit être une chaîne de caractères")
    if texte.strip() == "":
        raise ValueError("Le texte ne peut pas être vide")


def est_palindrome(mot):
    _verifier(mot)
    nettoye = "".join(c.lower() for c in mot if c.isalnum())
    return nettoye == nettoye[::-1]


def compter_voyelles(texte):
    _verifier(texte)
    return sum(1 for c in texte.lower() if c in VOYELLES)


def inverser(texte):
    _verifier(texte)
    return texte[::-1]


@texte_bp.get("/palindrome")
def route_palindrome():
    mot = request.args.get("mot")

    # Vérifier que le paramètre existe
    if mot is None:
        return erreur_400("Le paramètre mot est obligatoire")

    try:
        return jsonify({"mot": mot, "resultat": est_palindrome(mot)})
    except ValueError as e:
        return erreur_400(str(e))


@texte_bp.get("/voyelles")
def route_voyelles():
    texte = request.args.get("texte")

    # Vérifier que le paramètre existe
    if texte is None:
        return erreur_400("Le paramètre texte est obligatoire")

    try:
        return jsonify({"texte": texte, "resultat": compter_voyelles(texte)})
    except ValueError as e:
        return erreur_400(str(e))


@texte_bp.get("/inverser")
def route_inverser():
    texte = request.args.get("texte")

    # Vérifier que le paramètre existe
    if texte is None:
        return erreur_400("Le paramètre texte est obligatoire")

    try:
        return jsonify({"texte": texte, "resultat": inverser(texte)})
    except ValueError as e:
        return erreur_400(str(e))