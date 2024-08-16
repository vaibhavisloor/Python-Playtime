from flask import Flask, render_template, redirect, url_for
from forms import LoginForm

app = Flask(__name__)
app.secret_key = 'secret_key_here'  # Necessary for CSRF protection

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Process login here
        print(form.username.data)
        print(form.password.data)
        return redirect(url_for('success'))
    return render_template('login.html', form=form)

@app.route('/success')
def success():
    return "Logged in successfully!"

if __name__ == '__main__':
    app.run(debug=True)