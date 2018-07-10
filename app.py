from tornado.web import Application
from tornado.ioloop import IOLoop
from resources.item import TodoItem, TodoItems


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
    # import and run database
    run_server()
