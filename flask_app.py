# ---------------------------------------------------------------
#  Mon premier site Web avec Flask
# ---------------------------------------------------------------

from flask import Flask, render_template, request

app = Flask(__name__)

@app.get("/")
def accueil():
    return render_template("accueil.html")

@app.get("/presentation")
def presentation():
    mes_loisirs = [
        "La musculation",
        "La photographie urbaine dans Paris",
        "Le développement de ma marque de streetwear (The.RifBrand)"
    ]
    return render_template("presentation.html", prenom="Mehdi", nom="ERAHOUTEN", loisirs=mes_loisirs)

@app.get("/loisirs")
def loisirs():
    return "J'aime la musculation, la photographie urbaine dans les rues de Paris et gérer ma marque de streetwear."

# ---------------------------------------------------------------
#  Exercice 7 : Informations dans l'URL
# ---------------------------------------------------------------

@app.get("/bonjour/<prenom>")
def bonjour(prenom):
    # Utilise le template pour se protéger des injections (XSS)
    return render_template("bonjour.html", prenom=prenom)

@app.get("/calcul")
def calcul():
    # Récupération sécurisée des paramètres avec gestion d'erreur
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
    except ValueError:
        return "Erreur : Veuillez entrer uniquement des nombres entiers."

    op = request.args.get("op", "plus")

    if op == "fois":
        resultat = a * b
        symbole = "*"
    elif op == "moins":
        resultat = a - b
        symbole = "-"
    else:
        resultat = a + b
        symbole = "+"

    return f"{a} {symbole} {b} = {resultat}"

# ---------------------------------------------------------------
#  Lancement de l'application
# ---------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
