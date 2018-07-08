from tornado.web import RequestHandler
import json

# Project Imports
from utils import get_json_arg
from models.mysql import Items


class PageHandler(RequestHandler):
    def json_response(self, data, status_code=200):  # how many before *args?
        self.set_status(status_code)
        self.set_header("Content-Type", 'application/json')
        self.write(data)

    def json_error(self):
        self.json_response({'message': 'request body is empty'}, 404)

    def json_response_condition(self, **kwargs):
        if kwargs['condition']:
            self.json_response(kwargs['data'], kwargs['code'])
        else:
            self.json_error()


class TodoItems(PageHandler):
    def get(self):
        data = Items.query_all()
        self.json_response(json.dumps(data))


class TodoItem(PageHandler):
    def get(self, id=None):
        item = Items.query_single(int(id))
        self.json_response_condition(
            condition=id, data=json.dumps(item), code=200)

    def post(self):
        if self.request.body:
            item = get_json_arg(self.request.body, ['name'])
            Items.insert_single('name', item['name'])
            self.json_response({'message': 'item created'}, 201)
        else:
            self.json_error()

    def put(self, id):
        if self.request.body:
            item = get_json_arg(self.request.body, ['name'])
            Items.update_single('name', item['name'], int(id))
            self.json_response({'message': 'item updated'})
        else:
            self.json_error()

    def delete(self, id):
        Items.delete_single(id)
        message = {'message': 'Item with id {} was deleted'.format(id)}
        self.json_response(message)
