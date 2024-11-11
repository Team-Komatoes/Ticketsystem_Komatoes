from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect,
)  # pip install flask
import mysql.connector                          #pip install mysql-connector-python
import time                             
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


@app.route("/submit-ticket", methods=["POST"])
def submit():
    name = request.form["name"]
    station_id = request.form["station"]
    fehler_id = request.form["fehler"]
    ticket_inhalt = request.form["ticketfeld"]
    #prio_ = request.form["prio"]

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """ Insert INTO koma (Mitarbeiter, Abteilung, Fehler, Ticket)
            VALUES (%s, %s, %s, %s)""",
            (name, station_id, fehler_id, ticket_inhalt),
        )
        time.sleep(5)
        conn.commit()
        print("Ticket erfolgreich gespeichert!")
    except Error as e:
        print("Fehler beim Speichern des Tickets: ", e)
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

    return redirect ("/")


if __name__ == "__main__":
    app.run(debug=True)
