from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def show():
    return "Hi after a long time"


@app.route("/name/<name>")
def show_name(name):
    x = type(name)
    # return f"Hello {name}"
    return escape(x)

@app.route("/names/<name>")
def show_names(name):
    return name

if __name__ == "__main__":
    app.run(debug=True)