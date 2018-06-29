import MySQLdb

# instance, user, password, database
db = MySQLdb.connect("localhost", "root", "", "octopus-portal")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()
print("Database version : %s " % data)

db.close()
