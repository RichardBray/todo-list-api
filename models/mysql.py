import MySQLdb
import MySQLdb.cursors


class MySql:
    TABLE = ""

    @staticmethod
    def connect_to_db():
        return MySQLdb.connect(
            "localhost", "root", "", "todo_list",
            cursorclass=MySQLdb.cursors.DictCursor)

    @staticmethod
    def simpe_query(query):
        db = MySql.connect_to_db()
        cursor = db.cursor()
        cursor.execute(query)
        db.commit()
        db.close()

    @classmethod
    def insert_single(cls, *args):
        query = "INSERT INTO {} ({}) VALUES('{}')".format(
            cls.TABLE, args[0], args[1])
        MySql.simpe_query(query)

    @classmethod
    def query_all(cls):
        db = MySql.connect_to_db()
        cursor = db.cursor()

        query = "SELECT * FROM {}".format(cls.TABLE)
        cursor.execute(query)

        data = cursor.fetchall()
        db.close()
        print(data)
        return data  # returns tuple

    @classmethod
    def delete_single(cls, id):
        query = "DELETE FROM {} WHERE id={}".format(cls.TABLE, id)
        MySql.simpe_query(query)

    @classmethod
    def query_single(cls, id):
        db = MySql.connect_to_db()
        cursor = db.cursor()
        query = "SELECT * FROM {} WHERE id={}".format(cls.TABLE, id)
        cursor.execute(query)
        data = cursor.fetchall()
        db.close()
        return data


class Items(MySql):
    TABLE = "items"
