import pytest
from flask import Flask

from app.routes.texte import (
    compter_voyelles,
    est_palindrome,
    inverser,
    texte_bp,
)


@pytest.fixture
def client_texte():
    app = Flask(__name__)
    app.register_blueprint(texte_bp, url_prefix="/texte")
    app.config["TESTING"] = True
    
    return app.test_client()


# --- est_palindrome ---
def test_palindrome_normal():
    assert est_palindrome("kayak") is True


def test_palindrome_limite():
    assert est_palindrome("Esope reste ici et se repose") is True


def test_palindrome_erreur():
    with pytest.raises(ValueError):
        est_palindrome("")


# --- compter_voyelles ---
def test_voyelles_normal():
    assert compter_voyelles("bonjour") == 3


def test_voyelles_limite():
    assert compter_voyelles("ÉCOLE") == 3


def test_voyelles_erreur():
    with pytest.raises(ValueError):
        compter_voyelles(123)


# --- inverser ---
def test_inverser_normal():
    assert inverser("abc") == "cba"


def test_inverser_limite():
    assert inverser("a") == "a"


def test_inverser_erreur():
    with pytest.raises(ValueError):
        inverser("   ")


# --- routes ---
def test_route_palindrome_ok(client_texte):
    reponse = client_texte.get("/texte/palindrome", query_string={"mot": "kayak"})
    assert reponse.status_code == 200
    assert reponse.get_json()["resultat"] is True


def test_route_palindrome_invalide(client_texte):
    reponse = client_texte.get("/texte/palindrome", query_string={"mot": ""})
    assert reponse.status_code == 400


def test_route_voyelles_ok(client_texte):
    reponse = client_texte.get("/texte/voyelles", query_string={"texte": "bonjour"})
    assert reponse.status_code == 200
    assert reponse.get_json()["resultat"] == 3


def test_route_voyelles_parametre_absent(client_texte):
    reponse = client_texte.get("/texte/voyelles")
    assert reponse.status_code == 400


def test_route_inverser_ok(client_texte):
    reponse = client_texte.get("/texte/inverser", query_string={"texte": "abc"})
    assert reponse.status_code == 200
    assert reponse.get_json()["resultat"] == "cba"


def test_route_inverser_invalide(client_texte):
    reponse = client_texte.get("/texte/inverser", query_string={"texte": "   "})
    assert reponse.status_code == 400



    