# from tornado import httpserver
# from tornado import gen
# import tornado.web
from tornado.web import (Application, RequestHandler)
from tornado.ioloop import IOLoop
import json

items = []


def get_json_arg(req_body, fields):
    """
    Gets argument from JSON
    """
    results = {}
    for i in fields:
        results[i] = json.loads(req_body).get(i)
    return results


def get_filtered(id):
    """
    Filters list to pick one item
    """
    result = [item for item in items if item['id'] == int(id)]
    return result


class PageHandler(RequestHandler):
    def json_response(self, data, status_code=200):
        self.set_status(status_code)
        self.set_header("Content-Type", 'application/json')
        self.write(data)

    def json_error(self):
        self.json_response({'message': 'body is empty'}, 404)


class TodoItems(PageHandler):
    def get(self):
        self.json_response(json.dumps(items))


class TodoItem(PageHandler):

    def get(self, id=None):
        if id:
            item = get_filtered(id)
            self.json_response(json.dumps(item[0]))
        else:
            self.json_error()

    def post(self, id=None):
        print(id)
        if self.request.body:
            item = get_json_arg(self.request.body, ['name', 'id'])
            items.append(item)
            self.json_response(item, 201)
        else:
            self.json_error()

    def put(self, id):
        picked_item = get_filtered(id)
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


class InitialiseApp(Application):
    def __init__(self):
        handlers = [
            (r"/", TodoItems),
            (r"/api/v1/item/([^/]+)?", TodoItem)
        ]

        server_settings = {
            "debug": True,
            "autoreload": True
        }

        Application.__init__(self, handlers, **server_settings)


def run_server():
    app = InitialiseApp()
    app.listen(3000)
    IOLoop.instance().start()


if __name__ == '__main__':
    run_server()
