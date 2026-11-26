URL_EMAIL = "/validation/email_valide"


# --- Cas normal ---
def test_email_valide_format_correct(client):
    response = client.get(f"{URL_EMAIL}?email=test@mail.com")

    assert response.status_code == 200
    assert response.get_json() == {"email": "test@mail.com", "valide": True}