import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Database configuration
DB_CONFIG = {
    "dbname": "excuses_db",
    "user": "postgres",
    "password": "admin123",
    "host": "localhost",  # Change if your DB is hosted elsewhere
    "port": "5432"  # Default PostgresSQL port
}

def connect_to_db(user=DB_CONFIG["user"],
                  password=DB_CONFIG["password"],
                  host=DB_CONFIG["host"],
                  port=DB_CONFIG["port"]):
    conn = psycopg2.connect(user=user, password=password, host=host, port=port, dbname="excuses_db")
    cur = conn.cursor()
    return conn, cur

def create_db():
    try:
        conn = psycopg2.connect(user=DB_CONFIG["user"], password=DB_CONFIG["password"], host="localhost", port=5432)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute("CREATE DATABASE excuses_db;")
        conn.commit()
        cur.close()
        conn.close()
    except psycopg2.errors.DuplicateDatabase:
        print("Database >> excuses_db << found!")
    except Exception as e:
        print(str(e))

create_db()
