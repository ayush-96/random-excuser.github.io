from src.model.db.db_utils import connect_to_db


conn, cur = connect_to_db()

# Insert sample data
cur.execute("INSERT INTO excuses (text) VALUES ('My dog ate my homework.')")
cur.execute("INSERT INTO excuses (text) VALUES ('I got stuck in traffic.')")
cur.execute("INSERT INTO excuses (text) VALUES ('My internet was down.')")
cur.execute("INSERT INTO excuses (text) VALUES ('I overslept.')")
cur.execute("INSERT INTO excuses (text) VALUES ('I had a family emergency.')")

conn.commit()
cur.close()
conn.close()

print("Data loaded to the table")
