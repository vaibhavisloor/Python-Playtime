from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/login",methods=['POST'])
def receive_data():
    name = request.form["uname"]
    passw = request.form["pass"]
    print(name)
    print(passw)
    return render_template("value.html",name=name,passw=passw)

if __name__ == "__main__":
    app.run(debug=True)