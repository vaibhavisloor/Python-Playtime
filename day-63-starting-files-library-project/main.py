from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('book_collection.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    conn = get_db_connection()
    books = conn.execute('SELECT * FROM books').fetchall()
    print(books)  # Fetch all books from DB
    conn.close()
    return render_template('index.html', books=books)

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['name']
        author = request.form['author']
        rating = request.form['rating']

        # Insert new book into the database
        conn = get_db_connection()
        conn.execute('INSERT INTO books (title, author, rating) VALUES (?, ?, ?)', 
                     (title, author, rating))
        conn.commit()
        conn.close()

        return redirect(url_for('home'))  # Redirect back to home after adding the book

    return render_template('add.html')

if __name__ == "__main__":
    # Initialize the database with a table if it doesn't exist
    conn = get_db_connection()
    conn.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT NOT NULL UNIQUE, author TEXT NOT NULL, rating FLOAT NOT NULL)")
    conn.commit()
    conn.close()

    app.run(debug=True)
