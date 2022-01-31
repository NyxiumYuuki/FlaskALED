from flask import request, Blueprint
from werkzeug.exceptions import HTTPException
from .responses import send_message, send_error
from .api_functions import db_login, db_register, db_user_update, db_create_log, db_user_delete, db_admin_update_user, db_users

bp = Blueprint('myapp', __name__)


@bp.app_errorhandler(HTTPException)
def handle_exception(e):
    return send_error(e.code, e.name)


# Login
@bp.route('/api/login', methods=['POST'])
def login():
    post_json = request.json
    try:
        post_ip = str(post_json['ip'])
        post_email = str(post_json['email'])
        post_password = str(post_json['password'])
        if post_email != '' and post_password != '':
            res = db_login(post_ip, post_email, post_password)
            if res['status'] == 0:
                user = res['data']
                return send_message(res['message'], user)
            elif res['status'] == 1:
                return send_error(400, res['message'])
        else:
            return send_error(400, 'Empty email and/or password fields.')
    except KeyError as e:
        return send_error(400, 'Need email, password fields.')


# Register
@bp.route('/api/register', methods=['POST'])
def register():
    post_json = request.json
    try:
        post_ip = str(post_json['ip'])
        post_email = str(post_json['email'])
        post_nickname = str(post_json['nickname'])
        post_password = str(post_json['password'])
        if post_email != '' and post_password != '' and post_nickname != '':
            res = db_register(post_ip, post_email, post_nickname, post_password)
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
    post_json = request.json
    try:
        post_ip = str(post_json['ip'])
        post_user_id = str(post_json['user_id'])
        message = 'User disconnected.'
        db_create_log(
            ip=post_ip,
            action='logout',
            message=message,
            has_succeeded=True,
            status_code=0,
            table='users',
            id_user=post_user_id
        )
        return send_message(message, None, token_delete=True)
    except KeyError as e:
        return send_error(400, 'Need ' + str(e) + 'field.')


# Update User (Nickname, Password)
@bp.route('/api/user/update', methods=['PUT'])
def user_update():
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
            post_ip = str(post_json['ip'])
            post_user_id = str(post_json['user_id'])
            res = db_user_update(post_ip, post_user_id, post_nickname, post_password)
            if res['status'] == 1:
                return send_error(500, res['message'])
            elif res['status'] == 0:
                return send_message(res['message'], res['data'])
        else:
            return send_error(400, 'Empty nickname and/or password fields.')
    else:
        return send_error(400, 'Need ' + fields + 'field.')


# Delete User
@bp.route('/api/user/delete', methods=['DELETE'])
def user_delete():
    post_json = request.json
    try:
        post_ip = str(post_json['ip'])
        post_user_id = str(post_json['user_id'])
        res = db_user_delete(post_ip, post_user_id)
        if res['status'] != 0:
            return send_error(500, res['message'])
        else:
            db_create_log(
                ip=post_ip,
                action='delete',
                message='User deleted.',
                has_succeeded=True,
                status_code=0,
                table='users',
                id_user=post_user_id
            )
            return send_message(res['message'], None, token_delete=True)
    except KeyError as e:
        return send_error(400, 'Need ' + str(e) + 'field.')


# Admin : Create User
@bp.route('/api/admin/create/user', methods=['POST'])
def admin_create_user():
    post_json = request.json
    try:
        post_ip = str(post_json['ip'])
        post_user_id = str(post_json['user_id'])
        token_is_admin = str(post_json['token_is_admin'])
        if token_is_admin:
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
                    res = db_register(post_ip, post_email, post_nickname, post_password, is_admin=post_is_admin)
                    if res['status'] == 1:
                        db_create_log(
                            ip=post_ip,
                            action='admin/create/user',
                            message=res['message'],
                            has_succeeded=False,
                            status_code=res['status'],
                            table='users',
                            id_user=post_user_id
                        )
                        return send_error(500, res['message'])
                    elif res['status'] == 0:
                        db_create_log(
                            ip=post_ip,
                            action='admin/create/user',
                            message=res['message'],
                            has_succeeded=True,
                            status_code=res['status'],
                            table='users',
                            id_user=post_user_id
                        )
                        return send_message(res['message'], res['data'])
                else:
                    return send_error(400, 'Empty email and/or nickname and/or password and/or is_admin fields.')
            else:
                return send_error(400, 'Need ' + fields + 'field.')
        else:
            return send_error(500, 'User does not have permission.')
    except KeyError as e:
        return send_error(400, 'Need ' + str(e) + 'field.')


# Admin : Change User password and/or role
@bp.route('/api/admin/update/user', methods=['PUT'])
def admin_update_user():
    post_json = request.json
    try:
        post_ip = str(post_json['ip'])
        post_user_id = str(post_json['user_id'])
        token_is_admin = str(post_json['token_is_admin'])
        if token_is_admin:
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
                    res = db_admin_update_user(post_ip, post_user_id_delete, post_is_admin, post_password)
                    if res['status'] == 1:
                        db_create_log(
                            ip=post_ip,
                            action='admin/update/user',
                            message=res['message'],
                            has_succeeded=False,
                            status_code=res['status'],
                            table='users',
                            id_user=post_user_id
                        )
                        return send_error(500, res['message'])
                    elif res['status'] == 0:
                        db_create_log(
                            ip=post_ip,
                            action='admin/update/user',
                            message=res['message'],
                            has_succeeded=True,
                            status_code=res['status'],
                            table='users',
                            id_user=post_user_id
                        )
                        return send_message(res['message'], res['data'])
                else:
                    return send_error(400, 'Empty is_admin and/or password fields.')
            else:
                return send_error(400, 'Need ' + fields + 'field.')
        else:
            return send_error(500, 'User does not have permission.')
    except KeyError as e:
        return send_error(400, 'Need ' + str(e) + 'field.')


# Admin : Delete User
@bp.route('/api/admin/delete/user/<id>', methods=['DELETE'])
def admin_delete_user(id):
    post_json = request.json
    try:
        post_ip = str(post_json['ip'])
        post_user_id = str(post_json['user_id'])
        token_is_admin = str(post_json['token_is_admin'])
        if token_is_admin:
            post_json = {'id': id}
            post_user_id_delete = None
            fields = ''
            if 'id' in post_json:
                post_user_id_delete = int(post_json['id'])
            else:
                fields += 'id'
            if post_user_id_delete is not None:
                if str(post_user_id_delete) != '':
                    res = db_user_delete(post_ip, int(post_user_id_delete))
                    if res['status'] == 1:
                        db_create_log(
                            ip=post_ip,
                            action='admin/delete/user',
                            message=res['message'],
                            has_succeeded=False,
                            status_code=res['status'],
                            table='users',
                            id_user=post_user_id
                        )
                        return send_error(500, res['message'])
                    else:
                        db_create_log(
                            ip=post_ip,
                            action='admin/delete/user',
                            message=res['message'],
                            has_succeeded=True,
                            status_code=res['status'],
                            table='users',
                            id_user=post_user_id
                        )
                        return send_message(res['message'], None)
                else:
                    return send_error(400, 'Empty id field.')
            else:
                return send_error(400, 'Need ' + fields + 'field.')
        else:
            return send_error(500, 'User does not have permission.')
    except KeyError as e:
        return send_error(400, 'Need ' + str(e) + 'field.')


# List of User (must be authenticated) & Search
@bp.route('/api/users', methods=['GET'])
def users():
    get_ip = request.args.get('ip')
    get_user_id = request.args.get('user_id')
    get_query = request.args.get('q')
    get_by = request.args.get('by')
    get_id = request.args.get('id')
    get_is_admin = request.args.get('is_admin')
    get_order_by = request.args.get('order_by')
    res = db_users(get_ip, get_user_id, get_query, get_by, get_id, get_is_admin, get_order_by)
    if res['status'] == 1:
        return send_error(500, res['message'])
    else:
        return send_message(res['message'], res['data'])
