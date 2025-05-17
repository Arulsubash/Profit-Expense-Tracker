from cs50 import SQL
from flask import Flask, render_template, request, redirect, session
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

app.secret_key = "your_secret_key"

#database
db = SQL("sqlite:///database.db")

#login
@app.route("/", methods=["GET","POST"])
def login():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        username_db = db.execute("SELECT username FROM users WHERE username = ?;", username)

        #validation:
        if not username_db:
            return render_template("login.html", name_error="Invalid username")

        password_db = db.execute("SELECT password FROM users WHERE username = ?;", username)

        if not check_password_hash(password_db[0]['password'], password):
            return render_template("login.html", pass_error="In-correct password!")

        session["username"] = username_db[0]["username"]
        return redirect("/home")
    return render_template("login.html")

#register
@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirm")

        #validate username:
        validator = db.execute("SELECT username FROM users WHERE username = ?;", username)
        if len(validator) != 0:
            return render_template("register.html",name_error="Username allready exist!")

        #confirm password match:
        if password != confirm:
            return render_template("register.html",password_error="Confirm password not match!")

        #insert userdata into database:
        db.execute("INSERT INTO users (username, password) VALUES (?, ?);", username, generate_password_hash(password))
        return redirect("/")
    return render_template("register.html")

@app.route("/forget", methods=["GET","POST"])
def forget():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirm")

        #validate username:
        validator = db.execute("SELECT username FROM users WHERE username = ?;", username)
        if len(validator) == 0:
            return render_template("forget.html",name_error="Username not exist!")

        #confirm password match:
        if password != confirm:
            return render_template("forget.html",password_error="Confirm password not match!")

        #insert updated data into database
        db.execute("UPDATE users SET password = ? WHERE username = ?;", generate_password_hash(password), username)
        return redirect("/")

    return render_template("forget.html")


#homepage:
@app.route("/home", methods=["GET","POST"])
def home():

    if request.method == "POST":
        discription = request.form.get("discription")
        type = request.form.get("type")
        amount = request.form.get("amount")

        db.execute("INSERT INTO data(username, type, discription, amount) VALUES(?, ?, ?, ?);", session["username"], type, discription, amount)

    datas = db.execute("SELECT * FROM data WHERE username = ?;", session["username"])

    total = 0

    for data in datas:
        if data["type"] == "debit":
            total -= data["amount"]
        else:
            total += data["amount"]

    return render_template("home.html", name=session["username"], datas=datas, total=total)

#logout
@app.route("/logout", methods=["GET","POST"])
def logout():
    session.clear()
    return redirect("/")

#delete
@app.route("/clear", methods=["GET","POST"])
def clear():
    if request.method == "POST":
        clear= request.form.get("delete")

        if clear:
            db.execute("DELETE FROM data WHERE username = ? AND discription LIKE ?;", session["username"] ,f"%{clear}%")
            return redirect("/home")

#search
@app.route("/search", methods=["GET","POST"])
def search():
    if request.method == "POST":
        search = request.form.get("search")
        like = f"%{search}%"

        #search opration:
        if search:
            data = db.execute("SELECT * FROM data WHERE username = ? AND (discription LIKE ? OR type = ? OR amount = ?);", session["username"], like, search, search)
            return render_template("home.html", name= session["username"], datas=data)

#clear all
@app.route("/clearall", methods=["GET","POST"])
def clearall():
    if request.method == "POST":
        clear= request.form.get("clearall")

        if clear:
            db.execute("DELETE FROM data WHERE username = ?;", session["username"])
            return redirect("/home")

if __name__ == "__main__":
    app.run()
