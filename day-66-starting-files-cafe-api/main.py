from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random 
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect("instance\cafes.db",check_same_thread=False)
cursor = connection.cursor()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/all")
def show_all():
    cursor.execute("select * from cafes")
    row = cursor.fetchall()
    return row
 
@app.route("/random")
def get_random_cafe():
    cursor.execute("select id from cafes order by id desc limit 1")
    id = cursor.fetchone()
    max_id = id[0]

    random_id = random.randint(1,max_id)

    cursor.execute('select * from cafes where id = ?',(random_id,))
    rows = cursor.fetchmany()
    return str(rows[0]) 
    

# HTTP GET - Read Record
@app.route("/location")
def get_cafe():
    location = request.args.get('location')
    cursor.execute('select * from cafes where location = ?',(location,))
    row = cursor.fetchall()

    if len(row) == 0:
        return "No such cafe available"
    else:
        return row

# HTTP POST - Create Record
@app.route("/add",methods=['POST'])
def add_cafe():
    name = request.args.get('name')
    location = request.args.get('location')

    if not name or not location:
        return "Missing parameters"
    else:
        cursor.execute('insert into cafes(name,location) values (?,?)',(name,location))
        connection.commit()
        return 'Cafe Successfully added'

# HTTP PUT/PATCH - Update Record
@app.route("/change/<int:id>",methods=["PATCH"])
def  make_change(id):
    new_location = request.args.get("location")
    cursor.execute("select id from cafes order by id desc limit 1")
    mid = cursor.fetchone()
    max_id = int(mid[0])

    if id >=0 and id <= max_id:
        cursor.execute("update cafes set location = ? where id = ? ",(new_location,id))
        connection.commit()
        return "Update successfully made"
    else:
        return "Index out of range"
# HTTP DELETE - Delete Record
@app.route("/delete/<int:id>")
def delete_record(id):
    cursor.execute("select id from cafes order by id desc limit 1")
    mid = cursor.fetchone()
    max_id = int(mid[0])

    if id >=0 and id <= max_id:
        cursor.execute("DELETE FROM cafes where id = ?",(id,))
        return "Successfully Deleted"
    else:
        return "Index out of range"


if __name__ == '__main__':
    app.run(debug=True)
