import logging
from flask import Flask, jsonify

app = Flask(__name__)

# Endpoint 1: "Hello World"
@app.route('/')
def hello_world():
    return "Hello World"

# Endpoint 2: Logs an error and returns a "Bad Request" response
@app.route('/error')
def trigger_error():
    app.logger.error("An error occurred!")  # Log an error message
    return jsonify({"error": "Bad Request"}), 400  # Return 400 status code and error message

if __name__ == '__main__':
    # Set logging level to DEBUG to see the logs in the terminal
    app.logger.setLevel(logging.DEBUG)
    app.run(debug=True)
