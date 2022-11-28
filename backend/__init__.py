from flask import Flask
from flask_cors import CORS
try:
    from .routes import routes
except:
    import routes

def create_app():
    app = Flask(__name__)
    app.secret_key = "#J5fdf?.,2548f,NMFSDFJ3kdf"

    app.register_blueprint(routes, url_prefix="/")

    CORS(app)
    return app
