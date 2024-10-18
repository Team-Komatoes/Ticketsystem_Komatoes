from flask import Flask, render_template, jsonify  # pip install flask
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="proj_koma",
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/test-db")
def test_db_connection():
    try:
        conn = get_db_connection()
        if conn.is_connected():
            return jsonify(
                {"status": "success", "message": "Database connection succssesfull"}
            )
    except Error as e:
        return jsonify({"status": "error", "message": str(e)})
    finally:
        if conn and conn.is_connected():
            conn.close()


if __name__ == "__main__":
    app.run(debug=True)

# bitte kommentare einfügen zu neuen dingen!
