import MySQLdb


def connect_to_db:
    return MySQLdb.connect("localhost", "root", "", "todo_list")


def query_execution:
    """
    Simple query execution
    """
    pass


class TodoItemsModel:
    @staticmethod
    def query_all():
        db = connect_to_db()
        cursor = db.cursor()
        items = []

        cursor.execute("SELECT * FROM items")
        result = cursor.fetchall()

        if len(result) != 0:
            for row in result:
                items.append({'id': row[0], 'name': row[1]})

        db.close()

        return items


class TodoItemModel:
    @staticmethod
    def insert_new_item(item):
        db = connect_to_db()
        cursor = db.cursor()
        query = "INSERT INTO items (name) VALUES('{}')".format(item['name'])
        cursor.execute(query)

        db.commit()
        db.close()

    def delete_item(id):
        # TODO need to finish this, needs static method
        db = connect_to_db()
        cursor = db.cursor()
        query = "DELETE FROM items WHERE id=?"
        cursor.execute(query)

        db.commit()
        db.close()
