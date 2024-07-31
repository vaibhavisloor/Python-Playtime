from flask import Flask
app=Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World !"

@app.route("/username/<name>/<int:age>")
def greet(name,age):
    return f"Welcome {name}. You are {age} years old. "
if __name__ == "__main__":
    app.run(debug=True)