import mysql.connector
from mysql.connector import Error


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="proj_koma",
    )


@app.route("/test-db")
def test_db_connection():
    try:
        conn = get_db_connection()
        if conn.is_connected():
            return jsonify(
                {"status": "success", "message": "Database connection successful!"}
            )
    except Error as e:
        return jsonify({"status": "error", "message": str(e)})
    finally:
        if conn and conn.is_connected():
            conn.close()
