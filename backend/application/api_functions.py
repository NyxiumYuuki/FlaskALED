import hashlib
import os
from datetime import datetime
from flask_sqlalchemy import inspect
from .users_model import Users, db
from .logs_model import Logs


def db_create_log(ip, action, message, has_succeeded, status_code, table=None, id_user=None):
    log = Logs(
        date=datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
        ip=ip,
        action=action,
        message=message,
        has_succeeded=has_succeeded,
        status_code=status_code,
        table=table,
        id_user=id_user
    )
    db.session.add(log)
    db.session.commit()
    return log.json()


def hash_password(salt, password):
    return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)


def db_login(ip, email, password):
    user = Users.query.filter(
        Users.email == email
    ).first()

    # Check User and Hash Pass
    if user and user.hash_pass == hash_password(user.salt, password):
        message = 'User authenticated.'
        db_create_log(
            ip=ip,
            action='login',
            message=message,
            has_succeeded=True,
            status_code=0,
            table='users',
            id_user=user.id
        )
        return {'status': 0, 'message': message, 'data': user.json()}
    else:
        message = f'Email or password invalid'
        db_create_log(
            ip=ip,
            action='login',
            message=message,
            has_succeeded=False,
            status_code=1,
            table='users',
            id_user=None
        )
        return {'status': 1, 'message': message}  # Email or password invalid


def db_register(ip, email, nickname, password, is_admin):
    user = Users.query.filter(
        Users.email == email
    ).first()
    if user:
        message = f'{email} already exist.'
        db_create_log(
            ip=ip,
            action='register',
            message=message,
            has_succeeded=False,
            status_code=1,
            table='users',
            id_user=None
        )
        return {'status': 1, 'message': message}  # User already exist

    # Salt Hash Pass with SHA256
    salt = os.urandom(32)
    hash_pass = hash_password(salt, password)

    user = Users(
        email=email,
        hash_pass=hash_pass,
        nickname=nickname,
        salt=salt,
        is_admin=is_admin
    )
    user_inspect = inspect(user)
    db.session.add(user)
    check_inspect = user_inspect.pending
    db.session.commit()

    # Add to logs
    if check_inspect:
        id_user = user.json()['id']
        message = 'User registered.'
        has_succeeded = True
        status_code = 0
    else:
        id_user = None
        message = 'Internal Error: User not registered.'
        has_succeeded = False
        status_code = 1

    db_create_log(
        ip=ip,
        action='register',
        message=message,
        has_succeeded=has_succeeded,
        status_code=status_code,
        table='users',
        id_user=id_user
    )
    if status_code == 0:
        return {'status': 0, 'message': message, 'data': user.json()}
    elif status_code == 1:
        return {'status': 1, 'message': message}


def db_user_update(ip, user_id, nickname, password):
    user = Users.query.filter(
        Users.id == user_id
    ).first()
    if user:
        has_succeeded = False
        status_code = 2
        if nickname and password:
            # Salt Hash Pass with SHA256
            salt = os.urandom(32)
            hash_pass = hash_password(salt, password)
            Users.query.filter(Users.id == user_id).update({'nickname': nickname, 'hash_pass': hash_pass, 'salt': salt})
            db.session.commit()
            message = 'User nickname and password updated.'
            has_succeeded = True
            status_code = 0
        elif nickname:
            Users.query.filter(Users.id == user_id).update({'nickname': nickname})
            db.session.commit()
            message = 'User nickname updated.'
            has_succeeded = True
            status_code = 0
        elif password:
            # Salt Hash Pass with SHA256
            salt = os.urandom(32)
            hash_pass = hash_password(salt, password)
            Users.query.filter(Users.id == user_id).update({'hash_pass': hash_pass, 'salt': salt})
            db.session.commit()
            message = 'User password updated.'
            has_succeeded = True
            status_code = 0
        else:
            message = 'Only nickname and/or password can be changed.'

        db_create_log(
            ip=ip,
            action='user_update',
            message=message,
            has_succeeded=has_succeeded,
            status_code=status_code,
            table='users',
            id_user=user_id
        )
        return {'status': status_code, 'message': message, 'data': user.json()}
    else:
        message = 'User do not exist.'
        db_create_log(
            ip=ip,
            action='user_update',
            message=message,
            has_succeeded=False,
            status_code=1,
            table='users',
            id_user=user_id
        )
        return {'status': 1, 'message': message}
