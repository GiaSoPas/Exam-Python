"""Main application file"""
import logging
from flask import Flask, make_response, send_from_directory, jsonify


app = Flask(__name__)

app.debug = True

handler = logging.FileHandler('app.log', encoding='UTF-8')

logging_format = logging.Formatter('%(asctime)s - %(levelname)s /'
                                   '- %(filename)s /'
                                   '- %(funcName)s - %(lineno)s - %(message)s')

handler.setFormatter(logging_format)

app.logger.addHandler(handler)


@app.route('/log')
def get_log():
    # directory = app.config.APP_PATH
    try:
        response = make_response(
            send_from_directory('.', 'app.log', as_attachment=True))
        return response
    except Exception as e:
        return jsonify({"code": "404", "message": "{}".format(e)})


@app.route('/')
def hello_world():
    return "Hello, world1!v.2"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
