from tornado.web import RequestHandler
import json

# Project Imports
from utils import get_json_arg, get_filtered
from models.item import TodoItemsModel
items = []


class PageHandler(RequestHandler):
    def json_response(self, data, status_code=200):
        self.set_status(status_code)
        self.set_header("Content-Type", 'application/json')
        self.write(data)

    def json_error(self):
        self.json_response({'message': 'body is empty'}, 404)


class TodoItems(PageHandler):
    def get(self):
        result = TodoItemsModel.query_all()
        self.json_response(json.dumps(result))


class TodoItem(PageHandler):

    def get(self, id=None):
        if id:
            item = get_filtered(id, items)
            self.json_response(json.dumps(item[0]))
        else:
            self.json_error()

    def post(self, id=None):
        if self.request.body:
            item = get_json_arg(self.request.body, ['name', 'id'])
            items.append(item)
            self.json_response(item, 201)
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
        global items
        new_items = [item for item in items if item['id'] != int(id)]
        items = new_items
        message = {'message': 'Item with id {} was deleted'.format(id)}
        self.json_response(message)
