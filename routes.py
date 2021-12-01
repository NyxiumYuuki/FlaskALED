from app import app
from responses import send_message, send_error


# Login
@app.route('/api/login', methods=['POST'])
def login():
    return send_message('Login not implemented', None)


# Register
@app.route('/api/register', methods=['POST'])
def register():
    return send_message('Register not implemented', None)


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
@app.route('/api/user/create', methods=['POST'])
def user_create():
    return send_message('User.create not implemented', None)


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


# List of User (must be authenticated)
@app.route('/api/users', methods=['GET'])
def users():
    return send_message('Users not implemented', None)


# Search User
@app.route('/api/users/search', methods=['POST'])
def users_search():
    return send_message('Users.search not implemented', None)
