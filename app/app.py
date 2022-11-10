from doctest import OutputChecker
import json
from flask import Flask, request, jsonify, render_template

from backend.relationship_extraction.relation_ext_code import extract_relationship, create_model


model = create_model()

app = Flask(__name__)

@app.route('/')
def home_page():
    example_embed='This string is from python'
    return render_template('index.html', embed=example_embed)

@app.route('/test', methods=['GET', 'POST'])
def testfn():
    # GET request
    if request.method == 'GET':
        message = {'greeting':'Hello from Python'}
        return jsonify(message)  # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200

@app.post('/text')
def put_get():

    print(request.data)
    
    print("Getting the relation...")

    relation = extract_relationship(json.loads(request.data), model)

    print("Displaying relation....")

    print(relation)

    return 'Success', 200

#Run the app:
if __name__ == "__main__":
     app.debug = True
     app.run()