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


def get_abteilungen():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT ID, Abteilung FROM abteilungen"
        )  # (SELECT * FROM `abteilungen`) ginge auch
        items = cursor.fetchall()
        return items
    except Error as e:
        print(e)
        return []
    finally:
        if conn and conn.is_connected():
            conn.close()


def get_Errors():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM fehler")
        items = cursor.fetchall()
        return items
    except Error as e:
        print(e)
        return []
    finally:
        if conn and conn.is_connected():
            conn.close()


@app.route("/")
def home():
    stations = get_abteilungen()
    errors = get_Errors()
    print("Errors: ", errors)
    return render_template("index.html", stations=stations, errors=errors)


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
