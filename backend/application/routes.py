from flask import current_app as app
from flask import request
from .responses import send_message, send_error
from .api_functions import db_login, db_register


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
            return send_message(res['message'], res['data'])
        elif res['status'] == 1:
            return send_error(404, res['message'])
    else:
        return send_error(400, 'POST Request Error : Need email, password fields.')


# Register
@app.route('/api/register', methods=['POST'])
def register():
    post_json = request.json
    post_email = str(post_json['email'])
    post_password = str(post_json['password'])
    post_is_admin = bool(post_json['is_admin'])

    if post_email and post_password and post_is_admin:
        ip = request.remote_addr
        res = db_register(ip, post_email, post_password, post_is_admin)
        if res['status'] == 1:
            return send_error(500, res['message'])
        elif res['status'] == 0:
            return send_message(res['message'], res['data'])
    else:
        return send_error(400, 'POST Request Error : Need email, password and is_admin fields.')


# Logout
@app.route('/api/logout', methods=['POST'])
def logout():
    return send_message('Logout not implemented', None)


# Update User
@app.route('/api/user/update', methods=['PUT'])
def user_update():
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
