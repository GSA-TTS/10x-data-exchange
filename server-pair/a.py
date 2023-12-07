from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return '<html><h1>Flask A</h1><a href="http://localhost:5002">to B</a></html>'
