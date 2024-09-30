from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']

        return f"Welcome {fname},{lname},{request.form}"

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)