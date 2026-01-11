from flask import Flask, redirect, request, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", title="SWPS Training Home")

@app.route("/about-me")
def about():
    return render_template("about-me.html", title="About Me")

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact")

if __name__ == "__main__":
    app.run(debug=True, port=3333)