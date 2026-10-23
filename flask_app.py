# ---------------------------------------------------------------
#  Mon premier site Web avec Flask
# ---------------------------------------------------------------
#  Ce fichier est le "cerveau" de votre site : c'est lui qui
#  reçoit les demandes des navigateurs et qui fabrique les réponses.
#
#  Vous allez le compléter petit à petit, exercice après exercice.
#  Les consignes sont dans le dossier "exercices/".
# ---------------------------------------------------------------

from flask import Flask

app = Flask(__name__)



# Une "route" associe une adresse (URL) à une fonction Python.
# Ici : quand quelqu'un visite la page d'accueil "/",
# Flask exécute la fonction accueil() et renvoie son résultat au navigateur.
@app.get("/")
def accueil():
   return "Bienvenue sur le site de Mehdi 🚀"


# ---------------------------------------------------------------
#  Ajoutez vos nouvelles routes ci-dessous 👇
# ---------------------------------------------------------------

@app.get("/presentation")
def presentation():
    return """
    <h1>Mehdi ERAHOUTEN</h1>
    <p>Je suis étudiant en <strong>Bachelor Informatique et Projets Numériques à l'ISEP</strong>.</p>
    <h2>Ce que j'aime</h2>
    <ul>
        <li>La musculation</li>
        <li>La photographie urbaine dans Paris</li>
        <li>Le développement de ma marque de streetwear (The.RifBrand)</li>
    </ul>
    <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="100">
    """
@app.get("/loisirs")
def loisirs():
    return "J'aime la musculation, la photographie urbaine dans les rues de Paris et gérer ma marque de streetwear."

# ---------------------------------------------------------------
#  Ne pas modifier : utile seulement pour lancer le site
#  sur votre propre ordinateur (python flask_app.py)
# ---------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
