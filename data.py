import psycopg2

try:
  conn = psycopg2.connect("dbname='myflaskapp' user=%s host='localhost' password=''" %('Casper'))
  print('success')
except:
  print("I am unable to connect to the database")

cur = conn.cursor()
cur.execute("INSERT INTO test(id) values(1)")
conn.commit()