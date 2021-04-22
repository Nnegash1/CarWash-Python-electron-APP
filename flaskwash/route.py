from flask import redirect, url_for,render_template, request
from flaskwash import app


@app.route("/workers", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        default_name = "None"
        workersName = request.form.get("fname",default_name)
        return render_template("list.html", workersName=workersName)
    return render_template("workers.html")

@app.route("/")
def index():
    return render_template("index.html")


