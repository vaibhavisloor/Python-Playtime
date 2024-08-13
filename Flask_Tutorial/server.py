from flask import Flask,render_template
import requests
import json

app=Flask(__name__)

@app.route("/guess/<name>")
def guess_age(name):
    params={
        "name" : name
    }
    endpoint = "https://api.agify.io/"
    response = (requests.get(endpoint,params=params)).json()
    return render_template("index.html",name=response["name"],age=response["age"])

if __name__ == "__main__":
    app.run(debug=True)