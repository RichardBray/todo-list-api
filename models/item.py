import MySQLdb


class TodoItemsModel():
    @staticmethod
    def query_all():
        db = MySQLdb.connect("localhost", "root", "", "todo_list")
        cursor = db.cursor()

        query = "SELECT * FROM items"
        cursor.execute(query)
        result = cursor.fetchall()
        items = []

        if type(result) is not tuple:
            for row in cursor.fetchall():
                items.append({'id': row[0], 'name': row[1]})

        db.close()
        return items
