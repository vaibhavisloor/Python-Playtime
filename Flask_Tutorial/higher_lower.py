from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0,9)
@app.route("/")
def home_page():
    return "Choose a number between 0-9 by using /number/(your number)"

@app.route("/number/<int:num>")
def higher_or_lower(num):
    if num < random_number:
        return "Lower"
    elif num > random_number:
        return "Higher"
    else:
        return f"You are correct . The number was {random_number}"
    
if __name__ == "__main__" :
    app.run(debug=True)
