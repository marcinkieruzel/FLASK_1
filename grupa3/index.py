# python -m venv .venv
# source .venv/bin/activate  (Linux/Mac)
# .venv\Scripts\activate     (Windows)
# pip install flask 


from flask import Flask, request, render_template, jsonify, session, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-sekretny-klucz-123'

@app.route("/")
def home():
    return render_template("index.html", title="Grupa jest najlepsza", list=['Ala', 'Ola', 'Ela'])

@app.route("/about")
def about():
    return "This is the About page for Grupa 3."

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'user' and password == 'pass':
        session['user'] = username
        return redirect('/dashboard')
    else:
        return redirect('/dashboard')


@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return f"Welcome to the dashboard, {session['user']}!"
    else:
        return "Please log in to access the dashboard."


if __name__ == "__main__":
    app.run(debug=True, port=5002)