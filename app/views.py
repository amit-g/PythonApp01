from datetime import datetime
from flask import Flask
from flask import render_template
from app.password import generate_random_password
from . import app

# app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
    return render_template(
        "hello_there.html",
        name = name,
        date = datetime.now()
    )

@app.route("/random/")
@app.route("/random/<name>")
def random(name = None):
    password = generate_random_password(12)
    return render_template(
        "random_password.html",
        password = password
    )

@app.route("/api/")
@app.route("/api/data")
def api_data():
    return app.send_static_file("data.json")
