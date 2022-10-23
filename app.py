from doctest import OutputChecker
import json
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
     return render_template('popup.html')

@app.route('/test', methods=['POST'])

def test():
     output = request.get_json()
     print(output)
     print(type(output))
     result = json.loads(output)
     print(result)
     print(type(result))
     return result


#Run the app:
if __name__ == "__main__":
     app.debug = True
     app.run()