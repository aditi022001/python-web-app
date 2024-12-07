from flask import Flask, jsonify

app = Flask(__name__)

# Endpoint 1: "Hello World"
@app.route('/')
def hello_world():
    return "Hello World"

# Endpoint 2: Logs an error and returns a "Bad Request" response
@app.route('/error')
def trigger_error():
    app.logger.error("An error occurred!")
    return jsonify({"error": "Bad Request"}), 400

if __name__ == '__main__':
    app.run(debug=True)
