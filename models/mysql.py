import MySQLdb

class MySql:
    TABLE = ""

    @staticmethod
    def connect_to_db:
        return MySQLdb.connect("localhost", "root", "", "todo_list")

    @classmethod
    def insert_single(cls, *args):
        db = connect_to_db()
        cursor = db.cursor()

        query = "INSERT INTO {} ({}) VALUES('{}')".format(cls.TABLE, args[0], args[1])
        cursor.execute(query)

        db.commit()
        db.close()

    @classmethod
    def query_all(cls, *args):
        db = connect_to_db()
        cursor = db.cursor()

        query = "SELECT * FROM {}".format(cls.TABLE)
        data = cursor.fetchall()
        db.close()

        return data


class Items(MySql):
    TABLE = "items"
