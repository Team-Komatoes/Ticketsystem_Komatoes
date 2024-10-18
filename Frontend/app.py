from flask import Flask, render_template, jsonify  # pip install flask
import mysql.connector
from mysql.connector import Error
from dbtest import test_db_connection, get_db_connection

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/test-db")
def test_db():
    result = test_db_connection
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)

# bitte kommentare einfügen zu neuen dingen!
