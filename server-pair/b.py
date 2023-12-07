from flask import Flask
from flask_cors import CORS

app = Flask(__name__, static_url_path="/static")
CORS(app)


@app.route("/")
def index():
    return """<!DOCTYPE html>
        <html>
            <h1>Flask B</h1>
            <p>
                <a href="http://localhost:5001">to A</a>
            </p>
            <p>
                <a href="static/image.jpg" download="image.jpg">
                    Same origin image
                </a>
            </p>
        </html>"""

@app.route("/data")
def data():
    return {"test": ["yes"]}
