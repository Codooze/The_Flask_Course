from os import name
from flask import Flask

app = Flask(__name__) #referencia este archivo

@app.route("/")
def index():
    return "Hello world"

if __name__ == "__main__":
    app.run(debug=True)