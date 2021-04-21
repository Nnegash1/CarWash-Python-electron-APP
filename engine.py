import sys
from flask import Flask, redirect, url_for,render_template, request

app = Flask(__name__)
name = ["Nahom", "Eyob", "Kifle"]

@app.route("/workers", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        default_name = "Np"
        workersName = request.form.get("fname",default_name)
        return render_template("list.html", workersName=workersName)
    return render_template("workers.html")

@app.route("/home")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.debug =True
    app.run(host='127.0.0.1', port=5000)
