import unittest
from flask_testing import TestCase
import json

from fictive_users import TAB_USER

from application import db, create_app
from application.users_model import Users
from application.logs_model import Logs




class BaseTestCase(TestCase):

    def create_app(self):
        app = create_app()
        return app


    def setUp(self):
        db.create_all()
        for user in TAB_USER:
            db.session.add(user)
        db.session.commit()


    def tearDown(self):
        db.session.remove()
        db.drop_all()




class FlaskTestCase(BaseTestCase):

    # -- UTILS ---

    def login(self, email, password):
        data0 = json.dumps({
            "email": email,
            "password": password
        })
        response = self.client.post('/api/login', data=data0)



    # --- LOGIN ---

    # def test_login_no_fields(self):
    #     data0 = {}
    #     response = self.client.post('/api/login', json={})
    #     print(response.json)
    #     self.assertEqual(response.json['message'], 'Need email, password fields.')


    # def test_login_empty_fields(self):
    #     data0 = {
    #         "email": "",
    #         "password": "blabla"
    #     }
    #     response = self.client.post('/api/login', json=data0)
    #     self.assertEqual(response.json['message'], 'Empty email and/or password fields.')


    def test_login_wrong_fields(self):
        data0 = {
            "email": "nimp@gmail.com",
            "password": "nimp"
        }
        response = self.client.post('/api/login', json=data0)
        print("------------")
        print(response)
        print("------------")
        self.assertEqual(response.json['message'], 'Email or password invalid')


    def test_login_success(self):
        data0 = {
            "email": "riri@gmail.com",
            "password": "ririPass"
        }
        response = self.client.post('/api/login', json=data0)
        print("------------")
        print(response)
        print("------------")
        self.assertEqual(response.json['message'], 'User authenticated.')



    # # --- REGISTER ---

    # def test_register_no_fields(self):
    #     data0 = json.dumps({})
    #     response = self.client.post('/api/register', data=data0)
    #     self.assertIn('Need', response.message)


    # def test_register_empty_fields(self):
    #     data0 = json.dumps({
    #         "email": "",
    #         "password": "blabla",
    #         "nickname": "blabla"
    #     })
    #     response = self.client.post('/api/register', data=data0)
    #     self.assertEqual(response.message, 'Empty email and/or password and/or nickname fields.')


    # def test_register_already_exist(self):
    #     data0 = json.dumps({
    #         "email": "riri@gmail.com",
    #         "password": "blabla",
    #         "nickname": "blabla"
    #     })
    #     response = self.client.post('/api/register', data=data0)
    #     self.assertIn('already exist', response.message)


    # def test_register_success(self):
    #     data0 = json.dumps({
    #         "email": "loulou@gmail.com",
    #         "password": "loulouPass",
    #         "nickname": "Loulou"
    #     })
    #     response = self.client.post('/api/register', data=data0)
    #     self.assertEqual(response.message, 'User registered.')



    # # --- LOGOUT ---

    # def test_logout_fail(self):
    #     response = self.client.delete('/api/logout')
    #     self.assertEqual(response.status_code, 500)


    # def test_logout_success(self):
    #     self.login_user()
    #     response = self.client.delete('/api/logout')
    #     self.assertEqual(response.status_code, 200)


    # # --- SELF UPDATE  ---

    # def test_self_update_not_connected(self):
    #     data0 = json.dumps({})
    #     response = self.client.put('/api/user/update', data=data0)
    #     self.assertEqual(response.status_code, 500)


    # def test_self_update_no_fields(self):
    #     self.login('riri@gmail.com', 'ririPass')
    #     data0 = json.dumps({})
    #     response = self.client.put('/api/user/update', data=data0)
    #     self.assertIn('Need', response.message)


    # def test_self_update_empty_fields(self):
    #     self.login('riri@gmail.com', 'ririPass')
    #     data0 = json.dumps({
    #         "nickname": "",
    #         "password": "blabla" 
    #     })
    #     response = self.client.put('/api/user/update', data=data0)
    #     self.assertEqual(response.message, 'Empty nickname and/or password fields.')
        

    # def test_self_update_success(self):
    #     self.login('riri@gmail.com', 'ririPass')
    #     data0 = json.dumps({
    #         "nickname": "Ririri",
    #         "password": "ririPass" 
    #     })
    #     response = self.client.put('/api/user/update', data=data0)
    #     self.assertEqual(response.status_code, 200)



    # # --- SELF DELETE  ---

    # def test_self_delete_not_connected(self):
    #     response = self.client.delete('/api/user/delete')
    #     self.assertEqual(response.status_code, 500)


    # def test_self_delete_success(self):
    #     self.login('donald@gmail.com', 'donaldPass')
    #     response = self.client.delete('/api/user/delete')
    #     self.assertEqual(response.status_code, 200)

    
    # def test_self_delete_last_admin(self):
    #     self.login('daisy@gmail.com', 'daisyPass')
    #     response = self.client.delete('/api/user/delete')
    #     self.assertEqual(response.message, 'Can\'t delete last admin')



    # # --- admin: CREATE USER ---

    # def test_admin_create_not_connected(self):
    #     data0 = json.dumps({})
    #     response = self.client.post('/api/admin/create/user', data=data0)
    #     self.assertEqual(response.message, 'User not authenticated.')

    
    # def test_admin_create_no_permission(self):
    #     self.login('riri@gmail.com', 'ririPass')
    #     data0 = json.dumps({})
    #     response = self.client.post('/api/admin/create/user', data=data0)
    #     self.assertEqual(response.message, 'User does not have permission.')


    # def test_admin_create_no_fields(self):
    #     self.login('daisy@gmail.com', 'daisyPass')
    #     data0 = json.dumps({})
    #     response = self.client.post('/api/admin/create/user', data=data0)
    #     self.assertIn('Need', response.message)

    
    # def test_admin_create_empty_fields(self):
    #     self.login('daisy@gmail.com', 'daisyPass')
    #     data0 = json.dumps({
    #         "email": "",
    #         "nickname": "Mickey",
    #         "password": "mickeyPass",
    #         "is_admin": true, 
    #     })
    #     response = self.client.post('/api/admin/create/user', data=data0)
    #     self.assertEqual(response.message, 'Empty email and/or nickname and/or password and/or is_admin fields.')


    # def test_admin_create_already_exist(self):
    #     self.login('daisy@gmail.com', 'daisyPass')
    #     data0 = json.dumps({
    #         "email": "riri@gmail.com",
    #         "passord": "blabla",
    #         "nickname": "blabla",
    #     })
    #     response = self.client.post('/api/admin/create/user', data=data0)
    #     self.assertIn('already exist', response.message)


    # def test_admin_create_success(self):
    #     self.login('daisy@gmail.com', 'daisyPass')
    #     data0 = json.dumps({
    #         "email": "mickey@gmail.com",
    #         "nickname": "Mickey",
    #         "password": "mickeyPass",
    #         "is_admin": true, 
    #     })
    #     response = self.client.post('/api/admin/create/user', data=data0)
    #     self.assertEqual(response.message, 'User registered.')
    


    # # --- admin: UPDATE USER ---

    # def test_admin_update_not_connected(self):
    #     data0 = json.dumps({})
    #     response = self.client.put('/api/admin/update/user', data=data0)
    #     self.assertEqual(response.message, 'User not authenticated.')

    
    # def test_admin_update_no_permission(self):
    #     self.login('riri@gmail.com', 'ririPass')
    #     data0 = json.dumps({})
    #     response = self.client.put('/api/admin/update/user', data=data0)
    #     self.assertEqual(response.message, 'User does not have permission.')


    # def test_admin_update_no_fields(self):
    #     self.login('daisy@gmail.com', 'daisyPass')
    #     data0 = json.dumps({})
    #     response = self.client.put('/api/admin/update/user', data=data0)
    #     self.assertIn('Need', response.message)

    
    # def test_admin_update_empty_fields(self):
    #     self.login('daisy@gmail.com', 'daisyPass')
    #     data0 = json.dumps({
    #         "id": 1,
    #         "password": "",
    #         "is_admin": false,
    #     })
    #     response = self.client.put('/api/admin/update/user', data=data0)
    #     self.assertEqual(response.message, 'Empty is_admin and/or password fields.')


    # def test_admin_update_not_exists(self):
    #     self.login('daisy@gmail.com', 'daisyPass')
    #     data0 = json.dumps({
    #         "id": 99,
    #         "password": "",
    #         "is_admin": false,
    #     })
    #     response = self.client.put('/api/admin/update/user', data=data0)
    #     self.assertEqual(response.message, 'User do not exist.')


    # def test_admin_update_success(self):
    #     self.login('daisy@gmail.com', 'daisyPass')
    #     data0 = json.dumps({
    #         "id": 1,
    #         "password": "roroPass",
    #         "is_admin": false, 
    #     })
    #     response = self.client.put('/api/admin/update/user', data=data0)
    #     self.assertEqual(response.status_code, 200)



    # # --- admin: DELETE USER ---

    # def test_admin_delete_not_connected(self):
    #     response = self.client.delete('/api/admin/delete/user')
    #     self.assertEqual(response.message, 'User not authenticated.')

    
    # def test_admin_delete_no_permission(self):
    #     self.login('riri@gmail.com', 'ririPass')
    #     response = self.client.delete('/api/admin/delete/user')
    #     self.assertEqual(response.message, 'User does not have permission.')


    # def test_admin_delete_no_fields(self):
    #     self.login('daisy@gmail.com', 'daisyPass')
    #     data0 = json.dumps({})
    #     response = self.client.delete('/api/admin/delete/user')
    #     self.assertIn('Need', response.message)

    
    # def test_admin_delete_not_exists(self):
    #     self.login('daisy@gmail.com', 'daisyPass')
    #     data0 = json.dumps({"id": 99})
    #     response = self.client.delete('/api/admin/delete/user')
    #     self.assertEqual(response.message, 'User do not exist.')

    
    # def test_admin_delete_success(self):
    #     self.login('daisy@gmail.com', 'daisyPass')
    #     data0 = json.dumps({"id": 2})
    #     response = self.client.delete('/api/admin/delete/user', data=data0)
    #     self.assertEqual(response.status_code, 200)



    # # --- LIST OF USER ---

    # def test_list_of_users_fail(self):
    #     response = self.client.get('/api/users')
    #     self.assertEqual(response.status_code, 500)


    # def test_list_of_users_success(self):
    #     self.login('riri@gmail.com', 'ririPass')
    #     response = self.client.get('/api/users')
    #     self.assertEqual(response.status_code, 200)





if __name__ == '__main__':
    unittest.main()
