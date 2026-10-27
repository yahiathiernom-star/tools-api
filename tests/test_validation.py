URL_EMAIL = "/validation/email_valide"


# --- Cas normal ---
def test_email_valide_format_correct(client):
    response = client.get(f"{URL_EMAIL}?email=test@mail.com")

    assert response.status_code == 200
    assert response.get_json() == {"email": "test@mail.com", "valide": True}


# --- Cas limites ---
def test_email_valide_sans_arobase(client):
    response = client.get(f"{URL_EMAIL}?email=testmail.com")

    assert response.status_code == 200
    assert response.get_json()["valide"] is False


def test_email_valide_sans_domaine(client):
    response = client.get(f"{URL_EMAIL}?email=toto@")

    assert response.status_code == 200
    assert response.get_json()["valide"] is False


def test_email_valide_espaces_autour(client):
    response = client.get(f"{URL_EMAIL}?email=%20test@mail.com%20")

    assert response.status_code == 200
    assert response.get_json() == {"email": "test@mail.com", "valide": True}


# --- Cas d'erreur ---
def test_email_valide_sans_parametre(client):
    response = client.get(URL_EMAIL)

    assert response.status_code == 400
    assert response.get_json()["erreur"] == "Le paramètre 'email' est requis"


def test_email_valide_parametre_vide(client):
    response = client.get(f"{URL_EMAIL}?email=%20%20")

    assert response.status_code == 400