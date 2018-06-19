# from tornado import httpserver
# from tornado import gen
# import tornado.web
from tornado.web import (Application, RequestHandler)
from tornado.ioloop import IOLoop  # input output loop
import json

items = []


def get_json_arg(req_body, arg):
    """
    Gets argument from JSON
    """
    return json.loads(req_body).get(arg)


class PageHandler(RequestHandler):
    def json_response(self, data, status_code=200):
        self.set_status(status_code)
        self.set_header("Content-Type", 'application/json')
        self.write(data)


class TodoItems(PageHandler):
    def get(self):
        self.json_response(json.dumps(items))


class TodoItem(PageHandler):
    def get(self, id):
        if id:
            item = list(filter(lambda item: item['id'] == int(id), items))
            # REVIEW Object of type 'filter' is not JSON serializable
            # This also needs to be a list
            self.json_response(json.dumps(item[0]))
        else:
            result = {'message': 'body is empty'}
            self.json_response(result, 404)

    def post(self):
        if self.request.body:
            name = get_json_arg(self.request.body, 'name')
            id = get_json_arg(self.request.body, 'id')
            item = {'id': id, 'name': name}
            items.append(item)
            self.json_response(item, 201)
        else:
            result = {'message': 'body is empty'}
            self.json_response(result, 404)

    def put(self, id):
        picked_item = list(filter(lambda item: item['id'] == int(id), items))
        # REVIEW TypeError: 'filter' object is not subscriptable
        # Making it a list fixed the error why?
        if picked_item:
            items.remove(picked_item[0])
            name = get_json_arg(self.request.body, 'name')
            item = {'id': int(id), 'name': name}
            items.append(item)
            self.json_response(item)

    def delete(self, id):
        global items
        new_items = list(filter(lambda item: item['id'] != int(id), items))
        items = new_items
        message = {'message': 'Item with id "{}" was deleted'.format(id)}
        self.json_response(message)


class InitialiseApp(Application):
    def __init__(self):
        handlers = [
            (r"/", TodoItems),
            (r"/api/v1/item/", TodoItem),
            (r"/api/v1/item/([^/]+)", TodoItem)
        ]

        server_settings = {
            "debug": True,
            "autoreload": True
        }

        Application.__init__(self, handlers, **server_settings)


def run_erver():
    app = InitialiseApp()
    app.listen(3000)
    IOLoop.instance().start()


if __name__ == '__main__':
    run_erver()
