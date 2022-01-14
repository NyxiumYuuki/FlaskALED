from flask import current_app as app
from flask import request, Blueprint
from flask_cors import CORS
from werkzeug.exceptions import HTTPException
from .responses import send_message, send_error
from .api_functions import db_login, db_register, db_user_update, db_create_log, db_user_delete, db_admin_update_user, db_users
from .sessionJWT import create_auth_token, check_auth_token

bp = Blueprint('myapp', __name__)
origin = app.config.get('ALLOW_ORIGIN')
if origin is None:
    origin = ['http://127.0.0.1:4200', 'http://localhost:4200']
CORS(bp, supports_credentials=True, origins=origin)


@bp.app_errorhandler(HTTPException)
def handle_exception(e):
    return send_error(e.code, e.name)


# Login
@bp.route('/api/login', methods=['POST'])
def login():
    post_json = request.json
    try:
        post_email = str(post_json['email'])
        post_password = str(post_json['password'])
        if post_email != '' and post_password != '':
            ip = request.remote_addr
            res = db_login(ip, post_email, post_password)
            if res['status'] == 0:
                user = res['data']
                token = create_auth_token(user)
                return send_message(res['message'], user, token)
            elif res['status'] == 1:
                user = None
                token = create_auth_token(user)
                return send_error(400, res['message'], token)
        else:
            return send_error(400, 'Empty email and/or password fields.')
    except KeyError as e:
        return send_error(400, 'Need email, password fields.')


# Register
@bp.route('/api/register', methods=['POST'])
def register():
    post_json = request.json
    try:
        post_email = str(post_json['email'])
        post_nickname = str(post_json['nickname'])
        post_password = str(post_json['password'])
        if post_email != '' and post_password != '' and post_nickname != '':
            ip = request.remote_addr
            res = db_register(ip, post_email, post_nickname, post_password)
            if res['status'] == 1:
                return send_error(500, res['message'])
            elif res['status'] == 0:
                return send_message(res['message'], res['data'])
        else:
            return send_error(400, 'Empty email and/or password and/or nickname fields.')
    except KeyError as e:
        return send_error(400, 'Need ' + str(e) + 'field.')


# Logout
@bp.route('/api/logout', methods=['DELETE'])
def logout():
    token = check_auth_token(request)
    if token['success']:
        ip = request.remote_addr
        message = 'User disconnected.'
        db_create_log(
            ip=ip,
            action='logout',
            message=message,
            has_succeeded=True,
            status_code=0,
            table='users',
            id_user=token['payload']['id']
        )
        return send_message(message, None, token_delete=True)
    else:
        return send_error(500, token['message'])


# Update User (Nickname, Password)
@bp.route('/api/user/update', methods=['PUT'])
def user_update():
    token = check_auth_token(request)
    if token['success']:
        post_json = request.json
        post_nickname = None
        post_password = None
        fields = ''
        if 'nickname' in post_json:
            post_nickname = str(post_json['nickname'])
        else:
            fields += 'nickname '

        if 'password' in post_json:
            post_password = str(post_json['password'])
        else:
            fields += 'password '

        if post_nickname is not None or post_password is not None:
            if post_nickname != '' and post_password != '':
                ip = request.remote_addr
                user_id = token['payload']['id']
                res = db_user_update(ip, user_id, post_nickname, post_password)
                if res['status'] == 1:
                    return send_error(500, res['message'])
                elif res['status'] == 0:
                    return send_message(res['message'], res['data'])
            else:
                return send_error(400, 'Empty nickname and/or password fields.')
        else:
            return send_error(400, 'Need ' + fields + 'field.')
    else:
        return send_error(500, token['message'])


# Delete User
@bp.route('/api/user/delete', methods=['DELETE'])
def user_delete():
    token = check_auth_token(request)
    if token['success']:
        ip = request.remote_addr
        user_id = token['payload']['id']
        res = db_user_delete(ip, user_id)
        if res['status'] != 0:
            return send_error(500, res['message'])
        else:
            db_create_log(
                ip=ip,
                action='delete',
                message='User deleted.',
                has_succeeded=True,
                status_code=0,
                table='users',
                id_user=token['payload']['id']
            )
            return send_message(res['message'], None, token_delete=True)
    else:
        return send_error(500, token['message'])


# Admin : Create User
@bp.route('/api/admin/create/user', methods=['POST'])
def admin_create_user():
    token = check_auth_token(request)
    if token['success']:
        ip = request.remote_addr
        user_id = token['payload']['id']
        is_admin = token['payload']['is_admin']
        if is_admin:
            post_json = request.json
            post_email = None
            post_nickname = None
            post_password = None
            post_is_admin = None
            fields = ''
            if 'email' in post_json:
                post_email = str(post_json['email'])
            else:
                fields += 'email '

            if 'nickname' in post_json:
                post_nickname = str(post_json['nickname'])
            else:
                fields += 'nickname '

            if 'password' in post_json:
                post_password = str(post_json['password'])
            else:
                fields += 'password '

            if 'is_admin' in post_json:
                post_is_admin = bool(post_json['is_admin'])
            else:
                fields += 'is_admin '

            if post_email is not None or post_nickname is not None or post_password is not None or post_is_admin is not None:
                if post_email != '' and post_nickname != '' and post_password != '' and str(post_is_admin) != '':
                    res = db_register(ip, post_email, post_nickname, post_password, is_admin=post_is_admin)
                    if res['status'] == 1:
                        db_create_log(
                            ip=ip,
                            action='admin/create/user',
                            message=res['message'],
                            has_succeeded=False,
                            status_code=res['status'],
                            table='users',
                            id_user=user_id
                        )
                        return send_error(500, res['message'])
                    elif res['status'] == 0:
                        db_create_log(
                            ip=ip,
                            action='admin/create/user',
                            message=res['message'],
                            has_succeeded=True,
                            status_code=res['status'],
                            table='users',
                            id_user=user_id
                        )
                        return send_message(res['message'], res['data'])
                else:
                    return send_error(400, 'Empty email and/or nickname and/or password and/or is_admin fields.')
            else:
                return send_error(400, 'Need ' + fields + 'field.')
        else:
            return send_error(500, 'User does not have permission.')
    else:
        return send_error(500, token['message'])


# Admin : Change User password and/or role
@bp.route('/api/admin/update/user', methods=['PUT'])
def admin_update_user():
    token = check_auth_token(request)
    if token['success']:
        user_id = token['payload']['id']
        is_admin = token['payload']['is_admin']
        if is_admin:
            post_json = request.json
            post_is_admin = None
            post_password = None
            post_user_id_delete = None
            fields = ''
            if 'id' in post_json:
                post_user_id_delete = int(post_json['id'])
            else:
                fields += 'id '

            if 'is_admin' in post_json:
                post_is_admin = bool(post_json['is_admin'])
            else:
                fields += 'is_admin '

            if 'password' in post_json:
                post_password = str(post_json['password'])
            else:
                fields += 'password '

            if post_user_id_delete is not None and (post_is_admin is not None or post_password is not None):
                if str(post_is_admin) != '' and post_password != '' and str(post_user_id_delete) != '':
                    ip = request.remote_addr
                    res = db_admin_update_user(ip, post_user_id_delete, post_is_admin, post_password)
                    if res['status'] == 1:
                        db_create_log(
                            ip=ip,
                            action='admin/update/user',
                            message=res['message'],
                            has_succeeded=False,
                            status_code=res['status'],
                            table='users',
                            id_user=user_id
                        )
                        return send_error(500, res['message'])
                    elif res['status'] == 0:
                        db_create_log(
                            ip=ip,
                            action='admin/update/user',
                            message=res['message'],
                            has_succeeded=True,
                            status_code=res['status'],
                            table='users',
                            id_user=user_id
                        )
                        return send_message(res['message'], res['data'])
                else:
                    return send_error(400, 'Empty is_admin and/or password fields.')
            else:
                return send_error(400, 'Need ' + fields + 'field.')
        else:
            return send_error(500, 'User does not have permission.')
    else:
        return send_error(500, token['message'])


# Admin : Delete User
@bp.route('/api/admin/delete/user/<id>', methods=['DELETE'])
def admin_delete_user(id):
    token = check_auth_token(request)
    if token['success']:
        ip = request.remote_addr
        user_id = token['payload']['id']
        is_admin = token['payload']['is_admin']
        if is_admin:
            post_json = {'id': id}
            post_user_id_delete = None
            fields = ''
            if 'id' in post_json:
                post_user_id_delete = int(post_json['id'])
            else:
                fields += 'id'
            if post_user_id_delete is not None:
                if str(post_user_id_delete) != '':
                    res = db_user_delete(ip, int(post_user_id_delete))
                    if res['status'] == 1:
                        db_create_log(
                            ip=ip,
                            action='admin/delete/user',
                            message=res['message'],
                            has_succeeded=False,
                            status_code=res['status'],
                            table='users',
                            id_user=user_id
                        )
                        return send_error(500, res['message'])
                    else:
                        db_create_log(
                            ip=ip,
                            action='admin/delete/user',
                            message=res['message'],
                            has_succeeded=True,
                            status_code=res['status'],
                            table='users',
                            id_user=user_id
                        )
                        return send_message(res['message'], None)
                else:
                    return send_error(400, 'Empty id field.')
            else:
                return send_error(400, 'Need ' + fields + 'field.')
        else:
            return send_error(500, 'User does not have permission.')
    else:
        return send_error(500, token['message'])


# List of User (must be authenticated) & Search
@bp.route('/api/users', methods=['GET'])
def users():
    token = check_auth_token(request)
    if token['success']:
        ip = request.remote_addr
        user_id = token['payload']['id']
        get_query = request.args.get('q')
        get_by = request.args.get('by')
        get_id = request.args.get('id')
        get_is_admin = request.args.get('is_admin')
        get_order_by = request.args.get('order_by')
        res = db_users(ip, user_id, get_query, get_by, get_id, get_is_admin, get_order_by)
        if res['status'] == 1:
            return send_error(500, res['message'])
        else:
            return send_message(res['message'], res['data'])
    else:
        return send_error(500, token['message'])
