from flask import Flask,render_template
import requests

app=Flask(__name__)


response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
response=response.json()

@app.route("/blog")
def home_page():
    return render_template("index.html",posts = response)

@app.route("/blog/<int:num>")
def get_blog(num):
    return render_template("blog.html",post=response[num])

if __name__ == "__main__":
    app.run(debug=True)