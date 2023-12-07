from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return '<html><h1>Flask B</h1><a href="http://localhost:5001">to A</a></html>'
