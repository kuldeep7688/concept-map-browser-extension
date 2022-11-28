from flask import Blueprint, request, render_template, session, jsonify
from flask import redirect, url_for
try:
    from backend.ml_rebel_pipeline import get_loaded_model_dict, get_triples
    from backend.ml_rebel_pipeline import save_network_html
except:
    from ml_rebel_pipeline import get_loaded_model_dict, get_triples
    from ml_rebel_pipeline import save_network_html

from flask import g


MODEL_DICT = get_loaded_model_dict()
print('\n\n\n')
print('Models loaded successfully...')
print('\n\n\n')

routes = Blueprint("routes", __name__)


@routes.route('/<id>')
def home_page(id):
    print('getting text')
    text = request.args.get('text')
    if text != None:
        session[id] = text
    if id in session:
        text = session[id]

    # parse text and call ml_pipeline.get_triples() here.
    # print('\n\n\n') 
    # print('The text is mentioned below : ')
    # print(text)
    kb = get_triples(text, MODEL_DICT)
    filename = "backend/templates/sample_network.html"
    save_network_html(kb, filename=filename)
    # print('\n\n\n')
    # return render_template('index.html', id=id)
    return render_template('sample_network.html')


# @routes.route('/<id>')
# def home_page(id):
#     text = request.args.get('text')
#     if text != None:
#         session[id] = text

#     if id in session:
#         text = session[id]

#     return redirect(url_for('routes.conceptmap'))


@routes.route('/test', methods=['GET', 'POST'])
def testfn():
    # GET request
    if request.method == 'GET':
        message = {'greeting':'Hello from Python'}
        return jsonify(message)  # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Success', 200


# @routes.route('/conceptmap', methods=['GET', 'POST'])
# def conceptmap():
#     text = request.args.get('text')
#     print('\n\n\n') 
#     print('The text is mentioned below : ')
#     print(text)
#     kb = get_triples(text, MODEL_DICT)
#     filename = "sample_network.html"
#     save_network_html(kb, filename=filename)
#     print('\n\n\n')
#     return render_template('sample_network.html')
