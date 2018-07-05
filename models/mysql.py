import MySQLdb

class MySql:
    TABLE = ""

    @staticmethod
    def connect_to_db():
        return MySQLdb.connect("localhost", "root", "", "todo_list")

    @staticmethod
    def simpe_query(query):
        db = MySql.connect_to_db()
        cursor = db.cursor()
        cursor.execute(query)
        db.commit()
        db.close()


    @classmethod
    def insert_single(cls, *args):
        query = "INSERT INTO {} ({}) VALUES('{}')".format(cls.TABLE, args[0], args[1])
        MySql.simpe_query(query)


    @classmethod
    def query_all(cls, *args):
        db = MySql.connect_to_db()
        cursor = db.cursor()

        query = "SELECT * FROM {}".format(cls.TABLE)
        cursor.execute(query)

        data = cursor.fetchall()
        db.close()

        return data


    @classmethod
    def delete_single(cls, id):
        query = "DELETE FROM {} WHERE id={}".format(cls.TABLE, id)
        MySql.simpe_query(query)


class Items(MySql):
    TABLE = "items"
