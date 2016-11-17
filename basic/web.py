#!/usr/bib/python3

from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return redirect(url_for('test'))


@app.route("/test")
def test():
    return "Hello World!\n"


@app.route('/user/<name>')
def user(name):
    return "<h1> Hello %s</h1>" % name


if __name__ == "__main__":
    app.run(debug=True)



    # __name__:retrouve le chemin d'execution du fichier
