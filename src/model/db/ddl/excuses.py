from src.model.db.db_utils import connect_to_db


conn, cur = connect_to_db()

cur.execute("DROP TABLE IF EXISTS excuses;")

cur.execute('''
    CREATE TABLE IF NOT EXISTS excuses (
        id SERIAL PRIMARY KEY,
        text VARCHAR(255) NOT NULL
    );
''')

conn.commit()
cur.close()
conn.close()

print("Table > excuses < created")
