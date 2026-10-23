# ---------------------------------------------------------------
#  Mon premier site Web avec Flask
# ---------------------------------------------------------------

from flask import Flask, render_template, request, redirect, abort

app = Flask(__name__)

# ---------------------------------------------------------------
#  Exercices précédents (Routes de base et templates)
# ---------------------------------------------------------------

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
#  Exercice 8 : Les formulaires (GET et POST)
# ---------------------------------------------------------------

@app.get("/formulaire")
def formulaire():
    return render_template("formulaire.html")

@app.route("/salut", methods=["GET", "POST"])
def salut():
    if request.method == "POST":
        prenom = request.form.get("prenom", "inconnu")
        ville = request.form.get("ville", "nulle part")
        couleur = request.form.get("couleur", "black")
    else:
        prenom = request.args.get("prenom", "inconnu")
        ville = request.args.get("ville", "nulle part")
        couleur = request.args.get("couleur", "black")
        
    return f"<h1 style='color: {couleur};'>Bonjour {prenom}, qui vient de {ville} ! (reçu en {request.method})</h1>"

# ---------------------------------------------------------------
#  Exercice 9 : Les codes de statut et d'erreur
# ---------------------------------------------------------------

@app.get("/home")
def home():
    # Redirection vers la page d'accueil
    return redirect("/")

@app.get("/secret")
def secret():
    # Bloque l'accès avec une erreur 403
    abort(403)

@app.errorhandler(404)
def page_introuvable(erreur):
    # Personnalisation de l'erreur 404 (Page non trouvée)
    return render_template("404.html"), 404

@app.errorhandler(403)
def acces_interdit(erreur):
    # Personnalisation de l'erreur 403 (Accès refusé)
    return render_template("403.html"), 403

# ---------------------------------------------------------------
#  Lancement de l'application
# ---------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
