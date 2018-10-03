import os
import MySQLdb


def create_all():
    # instance, user, password, database
    db = MySQLdb.connect("localhost", "root", "", "todo_list")
    os.enrion.get('DATABASE_URL', "localhost")

    cursor = db.cursor()

    create_table = """
                    DROP TABLE IF EXISTS items;
                    CREATE TABLE items (
                    id int(9) auto_increment primary key,
                    name char(20))"""

    cursor.execute(create_table)

    results = cursor.fetchall()

    print(results)
    # data = cursor.fetchone()  # Fetch a single row
    # print("Database version : %s " % data)

    db.close()
