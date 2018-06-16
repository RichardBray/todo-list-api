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
    # json.loads(self.request.body).get('name')
    return json.loads(req_body).get(arg)


class PageHandler(RequestHandler):
    def json_response(self, data, status_code):
        self.set_status(status_code)
        self.set_header("Content-Type", 'application/json')
        self.write(data)


class TodoItems(PageHandler):
    def get(self):
        self.json_response(json.dumps(items), 200)


class TodoItem(PageHandler):
    def get(self, name):
        if name:
            picked_item = filter(lambda item: item['name'] == name, items)
            self.json_response(picked_item, 200)
        else:
            result = {'message': 'body is empty'}
            self.json_response(result, 404)

    def post(self):
        if self.request.body:
            name = get_json_arg(self.request.body, 'name')
            item = {'name': name}
            items.append(item)
            self.json_response(item, 201)
        else:
            result = {'message': 'body is empty'}
            self.json_response(result, 404)


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


# def json_response(self, data):
#     self.set_header("Content-Type", 'application/json')
#     self.write(json_encode(data))
#     self.finish()


if __name__ == '__main__':
    run_erver()
