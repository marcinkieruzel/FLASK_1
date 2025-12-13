# python -m venv .venv
# source .venv/bin/activate  (Linux/Mac)
# .venv\Scripts\activate     (Windows)
# pip install flask
# 
from flask import Flask, request, render_template, jsonify, session, redirect



app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-sekretny-klucz-123'


list = []

@app.route("/")
def home():
    return render_template("index.html", title="Training Home for SWPS")

@app.route("/about")
def about():
    list = ['JS', 'Python', 'Flask', 'Django']
    return render_template("about.html", skills=list)


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if(username == "admin" and password == "admin"):
        session['user'] = username
        return redirect('/dashboard')
    else:
        return redirect('/dashboard')
    

@app.route("/dashboard")
def dashboard():
    if 'user' in session:
        return f"Welcome to the dashboard, {session['user']}!"
    else:
        return "Please log in to access the dashboard."



@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return 'Jestem get request'
    
    elif request.method == "POST":
        return jsonify(request.form)
        return 'Jestem post request'
    
    

    return "Contact us at contact@trainingmodule.com"

@app.route("/contact/<name>/<int:id>")
def contact_person(name, id):
    return f"Contacting {name} with {id}..."



if __name__ == "__main__":
    app.run(debug=True, port=5555)