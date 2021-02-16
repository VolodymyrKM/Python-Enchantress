import psycopg2
from pprint import pprint

conn = psycopg2.connect(
    database='illia',
    user='illia',
    password='pass',
    host='localhost'

)

cursor = conn.cursor()
cursor.execute('SELECT name, email,  FROM users')

results = cursor.fetchall()

results2 = cursor.fetchall()

pprint(results)

conn.close()

