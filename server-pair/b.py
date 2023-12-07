from flask import Flask

app = Flask(__name__, static_url_path="/static")


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
                    Same origin
                </a>
            </p>
        </html>"""
