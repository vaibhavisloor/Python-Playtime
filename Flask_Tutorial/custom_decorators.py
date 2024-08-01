from flask import Flask
app=Flask(__name__)

def make_bold(function):
    def wrapper(*args,**kwargs):
        result = function(*args,**kwargs)
        return f"<b>{result}</b>"
    return wrapper 

@app.route("/")
@make_bold
def home_page():
    return "Welcome"

if __name__ == "__main__":
    app.run(debug=True)