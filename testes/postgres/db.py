import psycopg2 #pip install psycopg2

#connected to the db
con = psycopg2.connect(
    host = "N979TIINOV03",
    database = "testdb",
    user = "postgres",
    password = "postgres",
    port = 5432)

#cursor
cur = con.cursor()

cur.execute("select id, name from employees")
rows = cur.fetchall()

for r in rows:
    print(f"id {r[0]}, name {r[1]}") #[id, name]

cur.close()

con.close()