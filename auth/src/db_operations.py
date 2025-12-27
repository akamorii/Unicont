import psycopg2

conn = psycopg2.connect(
    host="127.0.0.1",
    port=5432,
    user="postgres",
    password="zxc",
    dbname="postgres"
)

cur = conn.cursor()
cur.execute("SELECT version();")
print(cur.fetchone())