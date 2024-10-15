from flask import Flask,render_template
import random 
app= Flask(__name__)

num = random.randint(0,9)

@app.route("/")
def home_page():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)