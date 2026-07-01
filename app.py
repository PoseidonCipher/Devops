from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🐳 Docker Practice App</h1>
    <p>Welcome! Your Flask application is running successfully.</p>

    <h3>Available Pages</h3>
    <ul>
        <li><a href="/about">About</a></li>
        <li><a href="/contact">Contact</a></li>
        <li><a href="/status">Status (JSON)</a></li>
    </ul>
    """

@app.route("/about")
def about():
    return """
    <h2>About This Project</h2>
    <p>This is a sample Flask application created for learning Docker.</p>
    """

@app.route("/contact")
def contact():
    return """
    <h2>Contact</h2>
    <p>Email: practice@example.com</p>
    """

@app.route("/status")
def status():
    return jsonify({
        "application": "Docker Practice",
        "framework": "Flask",
        "python_version": "3.12",
        "status": "Running",
        "message": "Congratulations! Your Docker container is working."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
