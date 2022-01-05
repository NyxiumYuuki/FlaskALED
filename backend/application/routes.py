from flask import current_app as app
from flask import request
from .responses import send_message, send_error
from .api_functions import db_login, db_register
from .sessionJWT import create_auth_token, check_auth_token


# Login
@app.route('/api/login', methods=['POST'])
def login():
    post_json = request.json
    post_email = str(post_json['email'])
    post_password = str(post_json['password'])
    if post_email and post_password:
        ip = request.remote_addr
        res = db_login(ip, post_email, post_password)
        # TODO: Token Authentication
        if res['status'] == 0:
            user = res['data']
            token = create_auth_token(user)
            return send_message(res['message'], user, token)
        elif res['status'] == 1:
            user = None
            token = create_auth_token(user)
            return send_error(404, res['message'], token)
    else:
        return send_error(400, 'POST Request Error : Need email, password fields.')


# Register
@app.route('/api/register', methods=['POST'])
def register():
    post_json = request.json
    try:
        post_email = str(post_json['email'])
        post_nickname = str(post_json['nickname'])
        post_password = str(post_json['password'])
        post_is_admin = bool(post_json['is_admin'])

        if post_email and post_nickname and post_password and post_is_admin:
            ip = request.remote_addr
            res = db_register(ip, post_email, post_nickname, post_password, post_is_admin)
            if res['status'] == 1:
                return send_error(500, res['message'])
            elif res['status'] == 0:
                return send_message(res['message'], res['data'])
    except KeyError as e:
        return send_error(400, 'POST Request Error : Need '+str(e)+' field.')


# Logout
@app.route('/api/logout', methods=['DELETE'])
def logout():
    token = check_auth_token(request)
    if token['success']:
        return send_message('User disconnected.', None, token_delete=True)
    else:
        return send_error(500, token['message'])


# Update User
@app.route('/api/user/update', methods=['PUT'])
def user_update():
    token = check_auth_token(request)
    return send_message('User.update not implemented', None)


# Delete User
@app.route('/api/user/delete', methods=['DELETE'])
def user_delete():
    return send_message('User.delete not implemented', None)


# Admin : Create User
@app.route('/api/admin/create/user/', methods=['POST'])
def user_create():
    return send_message('Admin.create.user not implemented', None)


# Admin : Change User password
@app.route('/api/admin/update/user/password', methods=['PUT'])
def admin_update_user_pwd():
    return send_message('Admin.update.user.password not implemented', None)


# Admin : Change User role
@app.route('/api/admin/update/user/role', methods=['PUT'])
def admin_update_user_role():
    return send_message('Admin.update.user.role not implemented', None)


# Admin : Delete User
@app.route('/api/admin/delete/user', methods=['DELETE'])
def admin_delete_user():
    return send_message('Admin.delete.user not implemented', None)


# List of User (must be authenticated) & Search
@app.route('/api/users', methods=['GET'])
def users():
    return send_message('Users not implemented', None)
