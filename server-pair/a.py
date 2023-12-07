from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return """<!DOCTYPE html>
        <html>
            <h1>Flask A</h1>
            <p>
                <a href="http://localhost:5002">to B</a>
            </p>
            <p>
                <a href="http://localhost:5002/static/image.jpg" download="image.jpg">
                    Fetch across orgin
                </a>
            </p>
            </form>
        </html>"""
