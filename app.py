"""Main application file"""
import logging
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    logging.warning('Hello log')
    return "Hello, world1!v.2"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
