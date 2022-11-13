from flask import Blueprint, request, render_template, session

import random

routes = Blueprint("routes", __name__)

@routes.route("/")
def index():
    lol = random.randint(1, 10)
    text = request.args.get('bro')
    if text != None:
        session['i'] = text
    if 'i' in session:
        text = session['i']
    return render_template('sample_network.html', value=text, test=lol)
