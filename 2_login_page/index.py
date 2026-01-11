from flask import Flask, redirect, request, url_for, render_template, session

app = Flask(__name__)

app.secret_key = "supersecretkey"
users = {
    "alice": {"name": "Alice", "pass": "alice123"},
    "dave": {"name": "Dave", "pass": "dave123"},
    "eve": {"name": "Eve", "pass": "eve123"},
}


def find_user(username, password):
    user = users.get(username)
    if user and user["pass"] == password:
        return user
    return None


@app.route("/login", methods=["GET"])
def login_get():
    return render_template("login.html", title="Login Page")


@app.route("/login", methods=["POST"])
def login_post():
    username = request.form.get("email")
    password = request.form.get("password")

    if not username or not password:
        return "Username and password are required", 400

    session["user"] = find_user(username, password)
    session["logged_in"] = session["user"] is not None

    print(f"Attempted login with username: {username} and password: {password}")

    print(f"Login successful: {session['logged_in']} {session['user']}")

    if session["logged_in"]:
        return redirect(url_for("home"))

    return render_template("login.html", title="Login Page")


@app.route("/register", methods=["GET"])
def register():
    return render_template("register.html", title="Register Page")



@app.route("/register", methods=["POST"])
def register_post():
    email = request.form.get("email")
    password = request.form.get("password")
    password2 = request.form.get("password2")


    if password != password2:
        return "Passwords do not match", 400
    
    if email in users:
        return "User already exists", 400

    users.update({email: {"email": email, "pass": password}})

    print(users)

    print(
        f"Attempted registration with email: {email}, password: {password}, password2: {password2}"
    )

    return redirect(url_for("login_get"))


@app.route("/dashboard")
def home():
    if not session.get("logged_in"):
        return redirect(url_for("login_get"))
    return render_template(
        "dashboard.html", users=users, title="Dashboard", user=session.get("user")
    )


if __name__ == "__main__":
    app.run(debug=True, port=3333)
