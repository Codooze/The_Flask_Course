from app import app
from flask import render_template
# contendra todas nuestra vistas


@app.route("/")
def index():
    return render_template("public/index.html")


@app.route("/about")
def about():
    return "Estás about"
