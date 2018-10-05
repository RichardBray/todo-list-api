from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import json

items = []

class TodoItems(RequestHandler):
  def get(self):
    self.write({'items': items})


class TodoItem(RequestHandler):
  def post(self, _):
    items.append(json.loads(self.request.body))
    self.write({'message': 'new item added'})

  def delete(self, id):
    global items
    new_items = [item for item in items if item['id'] is not int(id)]
    items = new_items
    self.write({'message': 'Item with id %s was deleted' % id})


def make_app():
  urls = [
    ("/", TodoItems),
    (r"/api/item/([^/]+)?", TodoItem)
  ]
  return Application(urls, debug=True)
  
if __name__ == '__main__':
  app = make_app()
  app.listen(3000)
  IOLoop.instance().start()
