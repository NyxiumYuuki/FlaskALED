from flask import current_app as app
import json


def send_error(status_code, message):
    data_json = {
        'status': 'error',
        'message': message
    }
    res = app.response_class(
        response=json.dumps(data_json, sort_keys=True),
        status=status_code,
        mimetype='application/json'
    )
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res


def send_message(message, data):
    data_json = {
        'status': 'success',
        'message': message,
        'data': data
    }
    res = app.response_class(
        response=json.dumps(data_json, sort_keys=True),
        status=200,
        mimetype='application/json'
    )
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res
