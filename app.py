from flask import Flask, render_template, request
import pyjokes  

app = Flask(__name__)

@app.route("/")
def index():
    """
    Page d'accueil du site.
    Affiche une blague en français par défaut.
    """
    joke = pyjokes.get_joke(language="fr")  
    return render_template("index.html", joke=joke)  

@app.route("/joke")
def obtenir_blague():
    """
    Retourne une nouvelle blague en fonction de la langue choisie.
    La langue est récupérée via un paramètre GET dans l'URL.
    """
    langue = request.args.get("lang", "fr")  
    langues_supportees = {"fr": "fr", "en": "en", "es": "es"}  

 
    if langue not in langues_supportees:
        langue = "fr"

    joke = pyjokes.get_joke(language=langues_supportees[langue])  
    return joke  

if __name__ == "__main__":
    app.run(debug=True)  
