import psycopg2
#Establishing the connection
conn = psycopg2.connect(database="Prueba", user='postgres', password='diego666', host='127.0.0.1', port= '5432')
#Setting auto commit false
conn.autocommit = True
#Creating a cursor object using the cursor() method
cursor = conn.cursor()
# Preparing SQL queries to INSERT a record into the database.
cursor.execute('''INSERT INTO public."Bonoloto" VALUES ('prueba')''')
# Commit your changes in the database
conn.commit()
print("Records inserted........")
# Closing the connection
conn.close()