import random
from flask import Flask, jsonify, render_template
from model.db.db_utils import connect_to_db

app = Flask(__name__)


@app.route('/excuse', methods=['GET'])
def get_strings():
    try:
        conn, cur = connect_to_db()
        cur.execute("SELECT text FROM excuses;")
        results = cur.fetchall()
        cur.close()
        conn.close()

        excuse = {"text": results[random.randint(0, len(results)-1)]}
        return jsonify(excuse)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET'])
def index():
    return render_template(template_folder='.')

if __name__ == '__main__':
    app.run(debug=True)
