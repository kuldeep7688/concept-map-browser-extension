import app

@app.route("/", methods=["GET"])
def index():
    return "<h1>It works .</h1>"