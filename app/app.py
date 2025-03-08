import random
from flask import Flask, jsonify
from model.db.db_utils import connect_to_db

app = Flask(__name__)


@app.route('/strings', methods=['GET'])
def get_strings():
    try:
        conn, cur = connect_to_db()
        cur.execute("SELECT text FROM excuses;")
        results = cur.fetchall()
        cur.close()
        conn.close()

        return jsonify(results[random.randint(0, len(results)-1)])
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
