import re
from werkzeug.wrappers import response
from app import app
from datetime import datetime
from flask import render_template, request, redirect, jsonify, make_response

# contendra todas nuestra vistas

# * you can create custom filter in a new file and import them into your __init__


@app.template_filter("clean_date")  # -this is a custom template
def clean_date(dt):
    return dt.strftime("%d %b %Y")


@app.route("/")
def index():
    return render_template("public/index.html")


@app.route('/jinja')
def jinja():  # -Pasing python objects to the base template html
    my_name = "Jeison"
    age = 24
    langs = ["python", "java", "html", "css"]
    pets = {
        "Sasha": 4,
        "Mishu": 5,
        "Lucky": 8
    }
    colors = ("red", "green", 14)
    cool = True

    class GitRemote:
        def __init__(self, name, description, url) -> None:
            self.name = name
            self.description = description
            self.url = url

        def pull(self):
            return f"Pullin repo {self.name}"

        def clone(self):
            return f"Cloning into {self.url}"

    my_remote = GitRemote("flask Jinja", "Template desing tutorial", "https://github.com/jeison-AK/The_Flask_Course")

    def repeat(x, times):
        return x*times

    date = datetime.utcnow()
    return render_template("public/jinja.html", name=my_name,  # tienen que ser key=value para que pueda funcionar
                           age=age, langs=langs, pets=pets,
                           colors=colors, cool=cool,
                           GitRemote=GitRemote, my_remote=my_remote,  # podemos pasar una instance de la clase o la clase en si
                           repeat=repeat, date=date)


@app.route("/about")  # todo
def about():
    return render_template("public/about.html")


@app.route('/sign_up', methods=["GET", "POST"])  # to use this get post you need to import requests
def sing_up():
    # get to get the content and post to post it into our server
    # this code wiil execute only when the route recieve a post request
    if request.method == "POST":
        req = request.form
        # here we have several alternative to store what's in the form inside variables:
        username = req["username"]
        email = req.get("email")
        password = request.form["password"]
        print(username, email, password)
        return redirect(request.url)
    return render_template("public/sign_up.html")


users = {
    "mitsuhiko": {
        "name": "Armin Ronacher",
        "bio": "Creatof of the Flask framework",
        "twitter_handle": "@mitsuhiko"
    },
    "gvanrossum": {
        "name": "Guido Van Rossum",
        "bio": "Creator of the Python programming language",
        "twitter_handle": "@gvanrossum"
    },
    "elonmusk": {
        "name": "Elon Musk",
        "bio": "technology entrepreneur, investor, and engineer",
        "twitter_handle": "@elonmusk"
    }
}


@app.route('/profile/<username>')  # passing a variable with <> in the url
def profile(username):
    user = None
    if username in users:
        # print(users[username])
        user = users[username]
    return render_template("public/profile.html", username=username, user=user)


@app.route('/multiple/<foo>/<bar>/<baz>')
def multi(foo, bar, baz):
    return f"foo is {foo}, bar is {bar}, baz is {baz}"


@app.route("/json", methods=["POST"])
def json_example():
    if request.is_json:
        req = request.get_json()  # to get json data we use this
        # print(type(req))
        # print(req)
        response = {
            "message": "JSON received!!",
            "name": req.get("name")
        }
        res = make_response(jsonify(response), 200)  # converts lists dict strings and converts them to dictionaries
        return res
    else:
        res = make_response(jsonify({"message": "No Json received"}), 400)
        return res


@app.route('/guestbook')
def guestbook():
    return render_template("public/guestbook.html")


@app.route("/guestbook/create-entry", methods=["POST"])
def create_entry():

    req = request.get_json()

    print(req)

    res = make_response(jsonify(req), 200)

    return res
