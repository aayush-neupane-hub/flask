from flask import Flask,render_template,request,redirect,url_for

import sqlite3 as sql

conn = sql.connect("database.db",check_same_thread=False)
cursor = conn.cursor()


def create_table():
    quary = ''' CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        address TEXT NOT NULL
        )'''
        
    cursor.execute(quary)
    conn.commit()

create_table()    # Create table if not exists in the database

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    
    obj = cursor.execute("SELECT * FROM users")
    users = obj.fetchall()
    return render_template("index.html",users=users)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/insert_record",methods=["POST","GET"])
def insert_record():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        address = request.form.get("address")
        # print(f"Name: {name}, Email: {email}, Address: {address}")
        cursor.execute("INSERT INTO users (name,email,address) VALUES (?,?,?)",(name,email,address))
        conn.commit()
        return redirect(url_for("home"))
           
    else:
        return render_template("insert_record.html")
    

@app.route("/delete/<int:id>")
def delete(id):
    quary = "DELETE FROM users WHERE id = ?"
    cursor.execute(quary,(id,))
    conn.commit()
    return redirect(url_for("home"))



@app.route("/edit/<int:id>",methods=["POST","GET"])
def edit(id):
    quary = "SELECT * FROM users WHERE id = ?"
    cursor.execute(quary,(id,))
    user = cursor.fetchone()
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        address = request.form.get("address")
        quary = "UPDATE users SET name = ?, email = ?, address = ? WHERE id = ?"
        cursor.execute(quary,(name,email,address,id))
        conn.commit()
        return redirect("/")
    
    else:
        return render_template("edit_record.html",user=user)
    


if __name__ == "__main__": 
    app.run(debug=True, host="0.0.0.0", port=8000)