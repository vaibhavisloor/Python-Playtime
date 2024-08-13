from flask import Flask, render_template
import requests
from post import Post


app = Flask(__name__)
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
posts_list=[]
for post in posts:
    post_i = Post(post["id"],post["title"],post["subtitle"],post["body"])
    posts_list.append(post_i)

@app.route('/')
def home():
    return render_template("index.html",all_posts=posts_list)


@app.route("/post/<int:num>")
def single_post(num):
    for post in posts_list:
        if post.id == num:
            return render_template("post.html",post=post)
if __name__ == "__main__":
    app.run(debug=True)
