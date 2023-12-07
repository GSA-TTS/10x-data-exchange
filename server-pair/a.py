from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return """<!DOCTYPE html>
        <html>
            <script>
                async function getData() {
                    const obj = await fetch("http://localhost:5002/data");
                    console.log(obj)
                }
            </script>
            <h1>Flask A</h1>
            <p>
                <a href="http://localhost:5002">to B</a>
            </p>
            <p>
                <a href="http://localhost:5002/static/image.jpg" download="image.jpg">
                    Fetch image across orgin
                </a>
            </p>
            <p>
                <a href="#" onclick="getData()">Data</a>
            </p>
        </html>"""
