
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    example_embed='This string is from python'
    return render_template('sample_network.html')

if __name__ == "__main__":
     app.debug = True
     app.run()