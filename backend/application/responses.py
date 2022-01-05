from flask import current_app as app
import json


def send_error(status_code, message, token=None):
    data_json = {
        'status': 'error',
        'message': message
    }
    res = app.response_class(
        response=json.dumps(data_json),
        status=status_code,
        mimetype='application/json'
    )
    res.headers['Access-Control-Allow-Origin'] = app.config.get('ALLOW_ORIGIN')
    if token is not None:
        res.set_cookie('SESSIONID', token)
    return res


def send_message(message, data, token=None):
    data_json = {
        'status': 'success',
        'message': message,
        'data': data
    }
    res = app.response_class(
        response=json.dumps(data_json),
        status=200,
        mimetype='application/json'
    )
    res.headers['Access-Control-Allow-Origin'] = app.config.get('ALLOW_ORIGIN')
    if token is not None:
        res.set_cookie('SESSIONID', token)
    return res
