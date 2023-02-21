# from datetime import datetime
# from flask import Flask
# from flask import render_template
# from password import generate_password

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("home.html")

# @app.route("/about/")
# def about():
#     return render_template("about.html")

# @app.route("/contact/")
# def contact():
#     return render_template("contact.html")

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name = None):
#     return render_template(
#         "hello_there.html",
#         name = name,
#         date = datetime.now()
#     )

# @app.route("/password")
# def index():
#     password = generate_password(12)
#     return f'<h1>{password}</h1>'

# @app.route("/api/data")
# def get_data():
#     return app.send_static_file("data.json")
