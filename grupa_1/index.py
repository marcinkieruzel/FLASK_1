from flask import Flask, request, render_template, jsonify, session, redirect

app = Flask(__name__)

langs = ['Python', 'Flask', 'Django', 'JavaScript']

@app.route("/")
def home():
    return "Hello, World from SWPS Training!"

@app.route("/about")
def about():
    return "This is the About page for SWPS Training."

@app.route('/swps', methods=['GET'])
def swps():
    return render_template("index.html", title="SWPS Training Home", langs=langs)

@app.route('/form', methods=['GET'])
def form():
    return render_template("form.html")

@app.route('/swps', methods=['POST'])
def swps_post():
    global langs
    lang = request.form.get('lang')
    langs.append(lang)
    return "Dodano język", 201

if __name__ == "__main__":
    app.run(debug=True, port=3333)