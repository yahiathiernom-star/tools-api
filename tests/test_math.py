
def test_factorielle_normale(client):
    response = client.get("/math/factorielle?n=5")

    assert response.status_code == 200
    assert response.get_json() == {"resultat": 120}


def test_factorielle_limite(client):
    response = client.get("/math/factorielle?n=0")

    assert response.status_code == 200
    assert response.get_json() == {"resultat": 1}


def test_factorielle_erreur(client):
    response = client.get("/math/factorielle?n=-1")

    assert response.status_code == 400
