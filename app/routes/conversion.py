from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

from flask import Blueprint, jsonify, request

from app.erreurs import erreur_400

conversion_bp = Blueprint("conversion", __name__)

# Taux fixes indicatifs : nombre d'unités de devise étrangère pour 1 EUR.
TAUX_EUR = {
    "USD": Decimal("1.08"),
    "GBP": Decimal("0.84"),
    "XOF": Decimal("655.957"),
}


def _lire_nombre(parametre):
    valeur = request.args.get(parametre)
    if valeur is None:
        return None, erreur_400(f"Le paramètre {parametre} est obligatoire")

    try:
        nombre = Decimal(valeur)
    except (InvalidOperation, TypeError):
        return None, erreur_400(f"Le paramètre {parametre} doit être un nombre")

    if not nombre.is_finite():
        return None, erreur_400(f"Le paramètre {parametre} doit être un nombre fini")

    return nombre, None


def _json_nombre(nombre):
    return float(nombre)


@conversion_bp.get("/celsius_fahrenheit")
def celsius_fahrenheit():
    celsius, erreur = _lire_nombre("c")
    if erreur:
        return erreur

    fahrenheit = celsius * Decimal(9) / Decimal(5) + Decimal(32)
    return jsonify({"resultat": _json_nombre(fahrenheit)}), 200


@conversion_bp.get("/km_miles")
def km_miles():
    kilometres, erreur = _lire_nombre("km")
    if erreur:
        return erreur
    if kilometres < 0:
        return erreur_400("Le paramètre km doit être positif ou nul")

    miles = (kilometres * Decimal("0.621371")).quantize(
        Decimal("0.000001"), rounding=ROUND_HALF_UP
    )
    return jsonify({"resultat": _json_nombre(miles)}), 200


@conversion_bp.get("/euros_devise")
def euros_devise():
    montant, erreur = _lire_nombre("montant")
    if erreur:
        return erreur
    if montant < 0:
        return erreur_400("Le paramètre montant doit être positif ou nul")

    devise = request.args.get("devise")
    if devise is None:
        return erreur_400("Le paramètre devise est obligatoire")
    devise = devise.upper()

    if devise not in TAUX_EUR:
        devises = ", ".join(TAUX_EUR)
        return erreur_400(f"Devise non acceptée. Devises disponibles : {devises}")

    decimales = 0 if devise == "XOF" else 2
    quantum = Decimal(1).scaleb(-decimales)
    resultat = (montant * TAUX_EUR[devise]).quantize(
        quantum, rounding=ROUND_HALF_UP
    )
    return jsonify({"resultat": _json_nombre(resultat), "devise": devise}), 200
