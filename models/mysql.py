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

    @staticmethod
    def fetchall_query(query):
        db = MySql.connect_to_db()
        cursor = db.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        db.close()
        return data

    @classmethod
    def insert_single(cls, *args):
        query = "INSERT INTO {} ({}) VALUES('{}')".format(
            cls.TABLE, args[0], args[1])
        MySql.simpe_query(query)

    @classmethod
    def query_all(cls):
        query = "SELECT * FROM {}".format(cls.TABLE)
        return MySql.fetchall_query(query)

    @classmethod
    def delete_single(cls, id):
        query = "DELETE FROM {} WHERE id={}".format(cls.TABLE, id)
        MySql.simpe_query(query)

    @classmethod
    def query_single(cls, id):
        query = "SELECT * FROM {} WHERE id={}".format(cls.TABLE, id)
        return MySql.fetchall_query(query)

    @classmethod
    def update_single(cls, *args):
        query = "UPDATE {} SET {} = '{}' WHERE id = {}".format(
            cls.TABLE, args[0], args[1], args[2])
        MySql.simpe_query(query)


class Items(MySql):
    TABLE = "items"
