print('hashlib')
import hashlib

import os
from datetime import datetime

print('flask_sqlalchemy')
from flask_sqlalchemy import inspect

print('sqlalchemy')
from sqlalchemy import asc, desc, or_

print('users_model')
from .users_model import Users, db

print('logs_model')
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
    ).scalar()

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


def db_register(ip, email, nickname, password, is_admin=False):
    user = Users.query.filter(
        Users.email == email
    ).scalar()
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
    ).scalar()
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


def db_user_delete(ip, user_id):
    user_to_delete = Users.query.filter(Users.id == user_id).scalar()
    if user_to_delete:
        is_admin = bool(user_to_delete.json()['is_admin'])
        if is_admin and (Users.query.filter(Users.is_admin == True).count() <= 1 or user_id == 0):
            message = 'Can\'t delete last admin'
            db_create_log(
                ip=ip,
                action='user_delete',
                message=message,
                has_succeeded=False,
                status_code=2,
                table='users',
                id_user=user_id
            )
            return {'status': 2, 'message': message}
        else:
            test = Users.query.filter(Users.id == user_id).delete()
            if test == 1:
                db.session.commit()
                message = 'User deleted.'
                db_create_log(
                    ip=ip,
                    action='user_delete',
                    message=message,
                    has_succeeded=True,
                    status_code=0,
                    table='users',
                    id_user=user_id
                )
                return {'status': 0, 'message': message, 'data': None}
            else:
                message = 'User do not exist.'
                db_create_log(
                    ip=ip,
                    action='user_delete',
                    message=message,
                    has_succeeded=False,
                    status_code=1,
                    table='users',
                    id_user=user_id
                )
                return {'status': 1, 'message': message}
    else:
        message = 'User do not exist.'
        db_create_log(
            ip=ip,
            action='user_delete',
            message=message,
            has_succeeded=False,
            status_code=1,
            table='users',
            id_user=user_id
        )
        return {'status': 1, 'message': message}


def db_admin_update_user(ip, user_id, is_admin, password):
    user = Users.query.filter(
        Users.id == user_id
    ).scalar()
    if user:
        has_succeeded = False
        status_code = 2
        if is_admin is not None and password:
            # Salt Hash Pass with SHA256
            salt = os.urandom(32)
            hash_pass = hash_password(salt, password)
            Users.query.filter(Users.id == user_id).update({'is_admin': is_admin, 'hash_pass': hash_pass, 'salt': salt})
            db.session.commit()
            message = 'User is_admin and password updated.'
            has_succeeded = True
            status_code = 0
        elif is_admin is not None:
            Users.query.filter(Users.id == user_id).update({'is_admin': is_admin})
            db.session.commit()
            message = 'User is_admin updated.'
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
            message = 'Only is_admin and/or password can be changed.'

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


def db_users(ip, user_id, query, by='email,nickname', id=None, is_admin=None, order_by='email,asc'):
    # q= or id =
    # if q= then by= (default: email,nickname) or email or nickname
    # is_admin =
    # order_by = (default: email,asc), (nickname,asc), (id,desc), (is_admin,desc)

    users = Users.query
    if query is id and query is not None:
        message = 'Query or id field'
        db_create_log(
            ip=ip,
            action='users',
            message=message,
            has_succeeded=False,
            status_code=1,
            table='users',
            id_user=user_id
        )
        return {'status': 1, 'message': message}

    if query and by:
        if by == 'email':
            users = users.filter(Users.email.like('%' + query + '%'))
        elif by == 'nickname':
            users = users.filter(Users.nickname.like('%' + query + '%'))
        else:
            users = users.filter(or_(Users.nickname.like('%' + query + '%'), Users.email.like('%' + query + '%')))
    elif query and not by:
        users = users.filter(or_(Users.nickname.like('%' + query + '%'), Users.email.like('%' + query + '%')))
    elif id:
        users = users.filter(Users.id == id)
    else:
        pass

    if is_admin is not None:
        users = users.filter(Users.is_admin == is_admin)

    order_by = order_by.split(',')
    if order_by[0] == 'nickname':
        order = Users.nickname
    elif order_by[0] == 'id':
        order = Users.id
    elif order_by[0] == 'is_admin':
        order = Users.is_admin
    else:
        order = Users.email

    if len(order_by) > 1:
        if order_by[1] == 'asc':
            users = users.order_by(asc(order))
        elif order_by[1] == 'desc':
            users = users.order_by(desc(order))
        else:
            users = users.order_by(asc(order))
    else:
        users = users.order_by(asc(order))

    users = users.all()

    message = f'query({query}), by({by}), id({id}), is_admin({is_admin}) and order_by({order_by}): {len(users)} result(s)'
    db_create_log(
        ip=ip,
        action='users',
        message=message,
        has_succeeded=True,
        status_code=0,
        table='users',
        id_user=user_id
    )
    return {'status': 0, 'message': message, 'data': [user.json() for user in users]}
