from flask import Blueprint, request, render_template, session, jsonify
from backend.ml_pipeline import ml_pipeline

routes = Blueprint("routes", __name__)

# global variable to load models just once
MODEL_DICT = ml_pipeline.get_loaded_model_dict()

@routes.route('/')
def home_page():
    text = request.args.get('text')
    if text != None:
        session['i'] = text
    if 'i' in session:
        text = session['i']
    return render_template('index.html', embed = text)

@routes.route('/test', methods=['GET', 'POST'])
def testfn():
    # GET request
    if request.method == 'GET':
        message = {'greeting':'Hello from Python'}
        return jsonify(message)  # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200

@routes.route('/conceptmap', methods=['POST'])
def get_triples_from_ml_backend():
    input_text_dict = request.get_json(force=True)
    triples = ml_pipeline.get_triples(input_text_dict['text'], MODEL_DICT)
    print('\n\n\n')
    print('##########################################################')
    print(len(triples))
    print('##########################################################')
    print('\n\n\n')
    return jsonify(triples)
