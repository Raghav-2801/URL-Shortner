from flask import Flask, request, redirect, jsonify
import random
import sqlite3


def init_db():
    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            short_id TEXT PRIMARY KEY,
            long_url TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()
app = Flask(__name__)
init_db()

#next_url_path = 0
url_mappings = {}

letters = 'abcdefghijklmnopqrstuvwxyz'
number = '123456789'
Character = letters + number
shortened_length = 7

def generate_short_id():
    return ''.join(random.choice(Character) for _ in range(shortened_length))

@app.route('/shorten', methods=['POST'])
def create_new_short_url():
    # Validate request data
    if not request.json or 'url' not in request.json:
        return jsonify({'error': 'URL is required'}), 400
    
    long_url = request.json['url']
    short_id = generate_short_id()

    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()

    while True:
        cursor.execute(
            " SELECT 1 FROM urls WHERE short_id = ?",
            (short_id, )
        )
        if not cursor.fetchone():
            break
        short_id = generate_short_id()
    cursor.execute(
        "INSERT INTO urls (short_id, long_url) VALUES (?, ?)",
        (short_id, long_url)
    )

    conn.commit()
    conn.close()

    # while short_id in url_mappings:
    #     short_id = generate_short_id()
    # url_mappings[short_id] = long_url
    # #return short_url
    short_url = f'http://127.0.0.1:5000/s/{short_id}'
    return jsonify({'short_url': short_url, 'short_id': short_id}), 201
    #return {'short_url': f'/s/{short_id}'}

# @app.get('/<int:id>')
# def redirect_to_url(id):
#     pass

@app.get('/s/<id>')
def redirect_to_url(id):
    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT long_url FROM urls WHERE short_id = ?",
        (id,)
    )
    row = cursor.fetchone()

    conn.close()

    if row:
        return redirect(row[0])

    #return {"error": "Not found"}, 404
    return jsonify({"error": "Short URL not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
