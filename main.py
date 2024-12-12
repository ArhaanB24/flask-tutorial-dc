from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    variable = ""
    if request.method == "POST":
        firstname = request.form.get("firstname")
        variable = firstname
        print(f"Firstname: {firstname}")
    return render_template("index.html",variable = variable)

@app.route("/homepage")
def myhomepage():
    return render_template("newpage.html")

if __name__ == "__main__":
    app.run(debug=True)