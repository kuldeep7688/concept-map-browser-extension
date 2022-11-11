from flask import Blueprint, Flask

routes = Blueprint("routes", __name__)

@routes.route("/")
def index():

    print("In here")
    return "<h1>It works .</h1>"
