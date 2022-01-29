from datetime import datetime, timedelta
from flask import current_app as app
import jwt


def create_auth_token(user, time_second=1800):
    try:
        time = datetime.now()
        payload = {
            'exp': time + timedelta(days=0, seconds=time_second),
            'iat': time,
            'user': user
        }
        return jwt.encode(
            payload,
            app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )
    except Exception as e:
        return e


def decode_auth_token(auth_token):
    try:
        payload = jwt.decode(
            auth_token,
            app.config.get('SECRET_KEY'),
            algorithms='HS256'
        )
        return {'success': True, 'payload': payload['user']}
    except jwt.ExpiredSignatureError:
        return {'success': False, 'message': 'Signature expired . Please log in again.'}
    except jwt.InvalidTokenError as e:
        return {'success': False, 'message': 'User not authenticated.'}


def check_auth_token(request):
    token = request.cookies.get('SESSIONID')
    return decode_auth_token(token)
