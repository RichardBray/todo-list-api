from tornado.web import RequestHandler
import json

# Project Imports
from utils import get_json_arg, get_filtered
from models.mysql import Items

items = []


class PageHandler(RequestHandler):
    def json_response(self, data, status_code=200):
        self.set_status(status_code)
        self.set_header("Content-Type", 'application/json')
        self.write(data)

    def json_error(self):
        self.json_response({'message': 'request body is empty'}, 404)


class TodoItems(PageHandler):

    def get(self):
        """
        Query all comes back as tuple so this converts
        it to a list of dicts
        """
        table_data = Items.query_all()
        data = []

        if len(table_data) != 0:
            for row in table_data:
                data.append({'id': row[0], 'name': row[1]})

        self.json_response(json.dumps(data))


class TodoItem(PageHandler):

    def get(self, id=None):
        if id:
            item = Items.query_single(int(id))
            print(item, id)
            self.json_response(json.dumps(item))
        else:
            self.json_error()

    def post(self, id=None):
        if self.request.body:
            item = get_json_arg(self.request.body, ['name'])
            Items.insert_single('name', item['name'])
            self.json_response({'message': 'item created'}, 201)
        else:
            self.json_error()

    def put(self, id):
        picked_item = get_filtered(id, items)
        if picked_item:
            items.remove(picked_item[0])
            item = get_json_arg(self.request.body, ['name'])
            item['id'] = int(id)
            items.append(item)
            self.json_response(item)

    def delete(self, id):
        Items.delete_single(id)
        message = {'message': 'Item with id {} was deleted'.format(id)}
        self.json_response(message)
