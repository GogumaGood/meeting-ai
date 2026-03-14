import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="meeting_ai",
    user="postgres",
    password="password"
)

cursor = conn.cursor()