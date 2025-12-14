from flask import Flask, redirect, request, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", title="Training Home for SWPS")

if __name__ == "__main__":
    app.run(debug=True, port=3333)