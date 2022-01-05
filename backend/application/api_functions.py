import hashlib
import os
from datetime import datetime
from flask_sqlalchemy import inspect
from .users_model import Users, db
from .logs_model import Logs


def hash_password(salt, password):
    return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)


def db_login(ip, email, password):
    user = Users.query.filter(
        Users.email == email
    ).first()

    # Check User and Hash Pass
    if user and user.hash_pass == hash_password(user.salt, password):
        message = 'User authenticated.'
        log = Logs(
            date=datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
            id_user=user.id,
            ip=ip,
            table='users',
            action='login',
            message=message,
            has_succeeded=True,
            status_code=0
        )
        db.session.add(log)
        db.session.commit()
        return {'status': 0, 'message': message, 'data': user.json()}
    else:
        message = f'Email or password invalid'
        log = Logs(
            date=datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
            id_user=None,
            ip=ip,
            table='users',
            action='login',
            message=message,
            has_succeeded=False,
            status_code=2
        )
        db.session.add(log)
        db.session.commit()
        return {'status': 1, 'message': message}  # Email or password invalid


def db_register(ip, email, password, is_admin):
    user = Users.query.filter(
        Users.email == email
    ).first()
    if user:
        message = f'{email} already exist.'
        log = Logs(
            date=datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
            id_user=None,
            ip=ip,
            table='users',
            action='register',
            message=message,
            has_succeeded=False,
            status_code=1
        )
        db.session.add(log)
        db.session.commit()
        return {'status': 1, 'message': message}  # User already exist

    # Salt Hash Pass with SHA256
    salt = os.urandom(32)
    hash_pass = hash_password(salt, password)

    user = Users(
        email=email,
        hash_pass=hash_pass,
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

    log = Logs(
        date=datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
        id_user=id_user,
        ip=ip,
        table='users',
        action='register',
        message=message,
        has_succeeded=has_succeeded,
        status_code=status_code
    )
    db.session.add(log)
    db.session.commit()
    if status_code == 0:
        return {'status': 0, 'message': message, 'data': user.json()}
    elif status_code == 1:
        return {'status': 1, 'message': message}
