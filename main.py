from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


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
        
        return redirect(url_for("home"))
           
    else:    
        return render_template("insert_record.html")



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)