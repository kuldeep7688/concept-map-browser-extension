from flask import Flask, MethodView

class View(MethodView):
    def __init__():
        pass

class ContentMap:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        # app.before_request(...)
        view = View.as_view()

ext = ContentMap()

def create_app():
    app = Flask(__name__)
    ext.init_app(app)
    return app
