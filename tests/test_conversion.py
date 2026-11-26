def test_celsius_fahrenheit_normal(client):
    response = client.get("/conversion/celsius_fahrenheit?c=25")

    assert response.status_code == 200
    assert response.get_json() == {"resultat": 77.0}


def test_celsius_fahrenheit_limite(client):
    response = client.get("/conversion/celsius_fahrenheit?c=-40")

    assert response.status_code == 200
    assert response.get_json() == {"resultat": -40.0}


def test_celsius_fahrenheit_erreur(client):
    response = client.get("/conversion/celsius_fahrenheit?c=chaud")

    assert response.status_code == 400


def test_km_miles_normal(client):
    response = client.get("/conversion/km_miles?km=10")

    assert response.status_code == 200
    assert response.get_json() == {"resultat": 6.21371}


def test_km_miles_limite(client):
    response = client.get("/conversion/km_miles?km=0")

    assert response.status_code == 200
    assert response.get_json() == {"resultat": 0.0}


def test_km_miles_erreur(client):
    response = client.get("/conversion/km_miles?km=abc")

    assert response.status_code == 400


def test_euros_devise_normal(client):
    response = client.get("/conversion/euros_devise?montant=10&devise=USD")

    assert response.status_code == 200
    assert response.get_json() == {"resultat": 10.8, "devise": "USD"}


def test_euros_devise_limite(client):
    response = client.get("/conversion/euros_devise?montant=0&devise=XOF")

    assert response.status_code == 200
    assert response.get_json() == {"resultat": 0.0, "devise": "XOF"}


def test_euros_devise_erreur(client):
    response = client.get("/conversion/euros_devise?montant=10&devise=CAD")

    assert response.status_code == 400
