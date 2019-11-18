from flask import render_template

from app import app

@app.route("/")
def index():
    return render_template(
        "index.html", 
        title="Petite page d'essai",
        subtitle="Un site qui va vous en mettre plein la vue"
    )