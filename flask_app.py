from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def accueil():
   return "Bienvenue sur le site de Mehdi 🚀"

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
