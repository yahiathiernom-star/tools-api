# Mini API Python

API Flask avec des endpoints de mathématiques et de conversion.

## Installation et lancement

```bash
python -m pip install -r requirements.txt
python run.py
```

L'état de l'API est disponible sur `GET /sante`.

## Endpoints mathématiques

| Route | Paramètres | Résultat |
|---|---|---|
| `GET /math/factorielle` | `n` entier positif ou nul | `{"resultat": 120}` |
| `GET /math/est_premier` | `n` entier | `{"resultat": true}` |
| `GET /math/pgcd` | `a`, `b` entiers | `{"resultat": 4}` |

Les paramètres manquants ou invalides renvoient HTTP 400. Le PGCD de `0` et
`0` est considéré comme non défini et renvoie HTTP 400.

## Endpoints de conversion

| Route | Paramètres | Résultat |
|---|---|---|
| `GET /conversion/celsius_fahrenheit` | `c` température en °C | `{"resultat": 77.0}` |
| `GET /conversion/km_miles` | `km` distance en kilomètres | `{"resultat": 6.21371}` |
| `GET /conversion/euros_devise` | `montant`, `devise` (`USD`, `GBP` ou `XOF`) | `{"resultat": 10.8, "devise": "USD"}` |

Exemples :

```text
GET /conversion/celsius_fahrenheit?c=25
GET /conversion/km_miles?km=10
GET /conversion/euros_devise?montant=10&devise=USD
```

Les taux de change sont fixes et indicatifs : `1 EUR = 1.08 USD`,
`1 EUR = 0.84 GBP` et `1 EUR = 655.957 XOF`. USD et GBP sont arrondis à deux
décimales ; XOF est arrondi à l'unité. Les taux ne sont pas actualisés par une
source externe. Les montants et distances négatifs sont refusés ; les
températures négatives sont acceptées.

Toutes les routes renvoient HTTP 400 pour un paramètre obligatoire manquant,
une valeur non numérique ou une devise non prise en charge.

## Tests

```bash
python -m pytest
```
