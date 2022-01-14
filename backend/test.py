import unittest
from flask_testing import TestCase
import json

from fictive_users import TAB_USER_WITH_PASSWORD, uwp_to_user

from application import db, create_app
from application.users_model import Users
from application.logs_model import Logs




class BaseTestCase(TestCase):

    def create_app(self):
        app = create_app('testing')
        return app


    def setUp(self):
        db.drop_all()
        db.create_all()
        for uwp in TAB_USER_WITH_PASSWORD:
            db.session.add(uwp_to_user(uwp))   
        db.session.commit()


    def tearDown(self):
        db.session.remove()
        db.drop_all()




class FlaskTestCase(BaseTestCase):

    # -- UTILS ---

    def login(self, email, password):
        data0 = {
            "email": email,
            "password": password
        }
        response = self.client.post('/api/login', json=data0)
        return response



    # --- LOGIN ---

    def test_login_NoFields_statusCode(self):
        response = self.client.post('/api/login', json={})
        self.assertEqual(response.status_code, 400)


    def test_login_NoFields_message(self):
        response = self.client.post('/api/login', json={})
        self.assertEqual(response.json['message'], 'Need email, password fields.')


    def test_login_emptyFields_statusCode(self):
        data0 = {
            "email": "",
            "password": "blabla"
        }
        response = self.client.post('/api/login', json=data0)
        self.assertEqual(response.status_code, 400)


    def test_login_emptyFields_message(self):
        data0 = {
            "email": "",
            "password": "blabla"
        }
        response = self.client.post('/api/login', json=data0)
        self.assertEqual(response.json['message'], 'Empty email and/or password fields.')


    def test_login_wrongFields_statusCode(self):
        data0 = {
            "email": "nimp@gmail.com",
            "password": "nimp"
        }
        response = self.client.post('/api/login', json=data0)
        self.assertEqual(response.status_code, 404)


    def test_login_wrongFields_message(self):
        data0 = {
            "email": "nimp@gmail.com",
            "password": "nimp"
        }
        response = self.client.post('/api/login', json=data0)
        self.assertEqual(response.json['message'], 'Email or password invalid')


    def test_login_success_statusCode(self):
        data0 = {
            "email": "riri@gmail.com",
            "password": "ririPass"
        }
        response = self.client.post('/api/login', json=data0)
        self.assertEqual(response.status_code, 200)


    def test_login_success_message(self):
        data0 = {
            "email": "riri@gmail.com",
            "password": "ririPass"
        }
        response = self.client.post('/api/login', json=data0)
        self.assertEqual(response.json['message'], 'User authenticated.')



    # --- REGISTER ---

    def test_register_noFields_statusCode(self):
        response = self.client.post('/api/register', json={})
        self.assertEqual(response.status_code, 400)


    def test_register_noFields_message(self):
        response = self.client.post('/api/register', json={})
        self.assertIn('Need', response.json['message'])


    def test_register_emptyFields_statusCode(self):
        data0 = {
            "email": "",
            "password": "blabla",
            "nickname": "blabla"
        }
        response = self.client.post('/api/register', json=data0)
        self.assertEqual(response.status_code, 400)


    def test_register_emptyFields_message(self):
        data0 = {
            "email": "",
            "password": "blabla",
            "nickname": "blabla"
        }
        response = self.client.post('/api/register', json=data0)
        self.assertEqual(response.json['message'], 'Empty email and/or password and/or nickname fields.')


    def test_register_alreadyExist_statusCode(self):
        data0 = {
            "email": "riri@gmail.com",
            "password": "blabla",
            "nickname": "blabla"
        }
        response = self.client.post('/api/register', json=data0)
        self.assertEqual(response.status_code, 500)


    def test_register_alreadyExist_statusCode(self):
        data0 = {
            "email": "riri@gmail.com",
            "password": "blabla",
            "nickname": "blabla"
        }
        response = self.client.post('/api/register', json=data0)
        self.assertIn('already exist', response.json['message'])


    def test_register_success_statusCode(self):
        data0 = {
            "email": "loulou@gmail.com",
            "password": "loulouPass",
            "nickname": "Loulou"
        }
        response = self.client.post('/api/register', json=data0)
        self.assertEqual(response.status_code, 200)


    def test_register_success_message(self):
        data0 = {
            "email": "loulou@gmail.com",
            "password": "loulouPass",
            "nickname": "Loulou"
        }
        response = self.client.post('/api/register', json=data0)
        self.assertEqual(response.json['message'], 'User registered.')



    # --- LOGOUT ---

    def test_logout_fail_(self):
        response = self.client.delete('/api/logout')
        self.assertEqual(response.status_code, 500)


    def test_logout_success(self):
        response = self.login("riri@gmail.com", "ririPass")
        self.assertEqual(response.status_code, 200)
        response = self.client.delete('/api/logout')
        self.assertEqual(response.status_code, 200)



    # --- USER/UPDATE  ---

    def test_userUpdate_notConnected_statusCode(self):
        response = self.client.put('/api/user/update', json={})
        self.assertEqual(response.status_code, 500)


    def test_userUpdate_notConnected_message(self):
        response = self.client.put('/api/user/update', json={})
        self.assertEqual(response.json['message'], 'User not authenticated.')


    def test_userUpdate_noFields_statusCode(self):
        response = self.login("riri@gmail.com", "ririPass")
        self.assertEqual(response.status_code, 200)
        response = self.client.put('/api/user/update', json={})
        self.assertEqual(response.status_code, 400)


    def test_userUpdate_noFields_message(self):
        response = self.login("riri@gmail.com", "ririPass")
        self.assertEqual(response.status_code, 200)
        response = self.client.put('/api/user/update', json={})
        self.assertIn('Need', response.json['message'])


    def test_userUpdate_emptyFields_statusCode(self):
        response = self.login("riri@gmail.com", "ririPass")
        self.assertEqual(response.status_code, 200)
        data0 = {
            "nickname": "",
            "password": "blabla" 
        }
        response = self.client.put('/api/user/update', json=data0)
        self.assertEqual(response.status_code, 400)


    def test_userUpdate_emptyFields_message(self):
        response = self.login("riri@gmail.com", "ririPass")
        self.assertEqual(response.status_code, 200)
        data0 = {
            "nickname": "",
            "password": "blabla" 
        }
        response = self.client.put('/api/user/update', json=data0)
        self.assertEqual(response.json['message'], 'Empty nickname and/or password fields.')


    def test_self_update_success_statusCode(self):
        response = self.login("riri@gmail.com", "ririPass")
        self.assertEqual(response.status_code, 200)
        data0 = {
            "nickname": "Ririri",
            "password": "ririPass" 
        }
        response = self.client.put('/api/user/update', json=data0)
        self.assertEqual(response.status_code, 200)



    # --- USER/DELETE  ---

    def test_userDelete_notConnected_statusCode(self):
        response = self.client.delete('/api/user/delete')
        self.assertEqual(response.status_code, 500)


    def test_userDelete_notConnected_message(self):
        response = self.client.delete('/api/user/delete')
        self.assertEqual(response.json['message'], 'User not authenticated.')


    def test_userDelete_success_statusCode(self):
        response = self.login('riri@gmail.com', 'ririPass')
        self.assertEqual(response.status_code, 200)
        response = self.client.delete('/api/user/delete')
        self.assertEqual(response.status_code, 200)


    def test_userDelete_success_message(self):
        response = self.login('riri@gmail.com', 'ririPass')
        self.assertEqual(response.status_code, 200)
        response = self.client.delete('/api/user/delete')
        self.assertEqual(response.json['message'], 'User deleted.')


    def test_userDelete_lastAdmin_statusCode(self):
        response = self.login('donald@gmail.com', 'donaldPass')
        self.assertEqual(response.status_code, 200)
        response = self.client.delete('/api/user/delete')
        self.assertEqual(response.status_code, 200)
        response = self.login('daisy@gmail.com', 'daisyPass')
        self.assertEqual(response.status_code, 200)
        response = self.client.delete('/api/user/delete')
        self.assertEqual(response.status_code, 500)


    def test_userDelete_lastAdmin_message(self):
        response = self.login('donald@gmail.com', 'donaldPass')
        self.assertEqual(response.status_code, 200)
        response = self.client.delete('/api/user/delete')
        self.assertEqual(response.status_code, 200)
        response = self.login('daisy@gmail.com', 'daisyPass')
        self.assertEqual(response.status_code, 200)
        response = self.client.delete('/api/user/delete')
        self.assertEqual(response.json['message'], 'Can\'t delete last admin')



    # --- ADMIN/CREATE/USER ---

    def test_adminCreate_notConnected_statusCode(self):
        response = self.client.post('/api/admin/create/user', json={})
        self.assertEqual(response.status_code, 500)


    def test_adminCreate_notConnected_message(self):
        response = self.client.post('/api/admin/create/user', json={})
        self.assertEqual(response.json['message'], 'User not authenticated.')


    def test_adminCreate_noPermission_statusCode(self):
        response = self.login('riri@gmail.com', 'ririPass')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/api/admin/create/user', json={})
        self.assertEqual(response.status_code, 500)


    def test_adminCreate_noPermission_message(self):
        response = self.login('riri@gmail.com', 'ririPass')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/api/admin/create/user', json={})
        self.assertEqual(response.json['message'], 'User does not have permission.')


    def test_adminCreate_noFields_statusCode(self):
        response = self.login('daisy@gmail.com', 'daisyPass')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/api/admin/create/user', json={})
        self.assertEqual(response.status_code, 400)


    def test_adminCreate_noFields_message(self):
        response = self.login('daisy@gmail.com', 'daisyPass')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/api/admin/create/user', json={})
        self.assertIn('Need', response.json['message'])


    def test_adminCreate_emptyFields_statusCode(self):
        response = self.login('daisy@gmail.com', 'daisyPass')
        self.assertEqual(response.status_code, 200)
        data0 = {
            "email": "",
            "nickname": "Mickey",
            "password": "mickeyPass",
            "is_admin": True, 
        }
        response = self.client.post('/api/admin/create/user', json=data0)
        self.assertEqual(response.status_code, 400)


    def test_adminCreate_emptyFields_message(self):
        response = self.login('daisy@gmail.com', 'daisyPass')
        self.assertEqual(response.status_code, 200)
        data0 = {
            "email": "",
            "nickname": "Mickey",
            "password": "mickeyPass",
            "is_admin": True, 
        }
        response = self.client.post('/api/admin/create/user', json=data0)
        self.assertEqual(response.json['message'], 'Empty email and/or nickname and/or password and/or is_admin fields.')


    def test_adminCreate_alreadyExist_statusCode(self):
        response = self.login('daisy@gmail.com', 'daisyPass')
        self.assertEqual(response.status_code, 200)
        data0 = {
            "email": "riri@gmail.com",
            "passord": "blabla",
            "nickname": "blabla",
        }
        response = self.client.post('/api/admin/create/user', json=data0)
        self.assertEqual(response.status_code, 500)


    def test_adminCreate_alreadyExist_message(self):
        response = self.login('daisy@gmail.com', 'daisyPass')
        self.assertEqual(response.status_code, 200)
        data0 = {
            "email": "riri@gmail.com",
            "passord": "blabla",
            "nickname": "blabla",
        }
        response = self.client.post('/api/admin/create/user', json=data0)
        self.assertIn('already exist', response.json['message'])


    def test_adminCreate_success_statusCode(self):
        response = self.login('daisy@gmail.com', 'daisyPass')
        self.assertEqual(response.status_code, 200)
        data0 = {
            "email": "mickey@gmail.com",
            "nickname": "Mickey",
            "password": "mickeyPass",
            "is_admin": True, 
        }
        response = self.client.post('/api/admin/create/user', json=data0)
        self.assertEqual(response.status_code, 200)


    def test_adminCreate_success_message(self):
        response = self.login('daisy@gmail.com', 'daisyPass')
        self.assertEqual(response.status_code, 200)
        data0 = {
            "email": "mickey@gmail.com",
            "nickname": "Mickey",
            "password": "mickeyPass",
            "is_admin": True, 
        }
        response = self.client.post('/api/admin/create/user', json=data0)
        self.assertEqual(response.json['message'], 'User registered.')



    # --- ADMIN/UPDATE/USER ---

    def test_adminUpdate_notConnected_statusCode(self):
        response = self.client.put('/api/admin/update/user', json={})
        self.assertEqual(response.status_code, 500)


    def test_adminUpdate_notConnected_message(self):
        response = self.client.put('/api/admin/update/user', json={})
        self.assertEqual(response.json['message'], 'User not authenticated.')


    def test_adminUpdate_noPermission_statusCode(self):
        response = self.login('riri@gmail.com', 'ririPass')
        self.assertEqual(response.status_code, 200)
        response = self.client.put('/api/admin/update/user', json={})
        self.assertEqual(response.status_code, 500)


    def test_adminUpdate_noPermission_message(self):
        response = self.login('riri@gmail.com', 'ririPass')
        self.assertEqual(response.status_code, 200)
        response = self.client.put('/api/admin/update/user', json={})
        self.assertEqual(response.json['message'], 'User does not have permission.')


    def test_adminUpdate_noFields_statusCode(self):
        response = self.login('daisy@gmail.com', 'daisyPass')
        self.assertEqual(response.status_code, 200)
        response = self.client.put('/api/admin/update/user', json={})
        self.assertEqual(response.status_code, 400)


    def test_adminUpdate_noFields_message(self):
        response = self.login('daisy@gmail.com', 'daisyPass')
        self.assertEqual(response.status_code, 200)
        response = self.client.put('/api/admin/update/user', json={})
        self.assertIn('Need', response.json['message'])


    def test_adminUpdate_emptyFields_statusCode(self):
        response = self.login('daisy@gmail.com', 'daisyPass')
        self.assertEqual(response.status_code, 200)
        data0 = {
            "id": 1,
            "password": "",
            "is_admin": False,
        }
        response = self.client.put('/api/admin/update/user', json=data0)
        self.assertEqual(response.status_code, 400)


    def test_adminUpdate_emptyFields_message(self):
        response = self.login('daisy@gmail.com', 'daisyPass')
        self.assertEqual(response.status_code, 200)
        data0 = {
            "id": 1,
            "password": "",
            "is_admin": False,
        }
        response = self.client.put('/api/admin/update/user', json=data0)
        self.assertEqual(response.json['message'], 'Empty is_admin and/or password fields.')


    def test_adminUpdate_notExists_statusCode(self):
        response = self.login('daisy@gmail.com', 'daisyPass')
        self.assertEqual(response.status_code, 200)
        data0 = {
            "id": 99,
            "password": "blabla",
            "is_admin": False
        }
        response = self.client.put('/api/admin/update/user', json=data0)
        self.assertEqual(response.status_code, 500)        


    def test_adminUpdate_notExists_message(self):
        response = self.login('daisy@gmail.com', 'daisyPass')
        self.assertEqual(response.status_code, 200)
        data0 = {
            "id": 99,
            "password": "blabla",
            "is_admin": False
        }
        response = self.client.put('/api/admin/update/user', json=data0)
        self.assertEqual(response.json['message'], 'User do not exist.')   


    def test_adminUpdate_success_message(self):
        response = self.login('daisy@gmail.com', 'daisyPass')
        self.assertEqual(response.status_code, 200)
        data0 = {
            "id": 1,
            "password": "roroPass",
            "is_admin": False, 
        }
        response = self.client.put('/api/admin/update/user', json=data0)
        self.assertEqual(response.status_code, 200)


    def test_adminUpdate_success_statusCode(self):
        response = self.login('daisy@gmail.com', 'daisyPass')
        self.assertEqual(response.status_code, 200)
        data0 = {
            "id": 1,
            "password": "roroPass",
            "is_admin": False, 
        }
        response = self.client.put('/api/admin/update/user', json=data0)
        self.assertIn("updated", response.json['message'])



    # --- ADMIN/DELETE/USER ---

    def test_adminDelete_notConnected_statusCode(self):
        response = self.client.delete('/api/admin/delete/user/1')
        self.assertEqual(response.status_code, 500)


    def test_adminDelete_notConnected_message(self):
        response = self.client.delete('/api/admin/delete/user/1')
        self.assertEqual(response.json['message'], 'User not authenticated.')


    def test_adminDelete_noPermission_statusCode(self):
        response = self.login('riri@gmail.com', 'ririPass')
        self.assertEqual(response.status_code, 200)
        response = self.client.delete('/api/admin/delete/user/1')
        self.assertEqual(response.status_code, 500)


    def test_adminDelete_noPermission_message(self):
        response = self.login('riri@gmail.com', 'ririPass')
        self.assertEqual(response.status_code, 200)
        response = self.client.delete('/api/admin/delete/user/1')
        self.assertEqual(response.json['message'], 'User does not have permission.')


    def test_adminDelete_noFields_statusCode(self):
        response = self.login('daisy@gmail.com', 'daisyPass')
        self.assertEqual(response.status_code, 200)
        response = self.client.delete('/api/admin/delete/user')
        self.assertEqual(response.status_code, 404)


    def test_adminDelete_no_fields(self):
        response = self.login('daisy@gmail.com', 'daisyPass')
        self.assertEqual(response.status_code, 200)
        response = self.client.delete('/api/admin/delete/user')
        self.assertEqual('Not Found', response.json['message'])


    def test_adminDelete_notExists_statusCode(self):
        response = self.login('daisy@gmail.com', 'daisyPass')
        self.assertEqual(response.status_code, 200)
        response = self.client.delete('/api/admin/delete/user/99')
        self.assertEqual(response.status_code, 500)


    def test_adminDelete_notExists_message(self):
        response = self.login('daisy@gmail.com', 'daisyPass')
        self.assertEqual(response.status_code, 200)
        response = self.client.delete('/api/admin/delete/user/99')
        self.assertEqual(response.json['message'], 'User do not exist.')


    def test_adminDelete_success_statusCode(self):
        response = self.login('daisy@gmail.com', 'daisyPass')
        self.assertEqual(response.status_code, 200)
        response = self.client.delete('/api/admin/delete/user/2')
        self.assertEqual(response.status_code, 200)


    def test_adminDelete_success_message(self):
        response = self.login('daisy@gmail.com', 'daisyPass')
        self.assertEqual(response.status_code, 200)
        response = self.client.delete('/api/admin/delete/user/2')
        self.assertEqual(response.json['message'], 'User deleted.')



    # --- LIST OF USER ---

    def test_listOfUsers_fail(self):
        response = self.client.get('/api/users')
        self.assertEqual(response.status_code, 500)


    def test_listOfUsers_success(self):
        response = self.login('riri@gmail.com', 'ririPass')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/api/users?order_by=nickname')
        self.assertEqual(response.status_code, 200)




if __name__ == '__main__':
    unittest.main()
