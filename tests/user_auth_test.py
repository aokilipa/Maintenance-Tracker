import unittest
import json
import os
import pytest

from config import TestingConfig
from run import create_app
from resources.user import User
from flask import request, jsonify

@pytest.mark.unittest
class UserTest(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client
        self.ctx = self.app.test_request_context
        self.req = {  "id": 3,"fname": "Mary", "lname": "Doe", "email": "mary@gmail.com" }
        self.modified = {  "id": 3,"fname": "Mary", "lname": "Doe", "email": "susansue@gmail.com" }
        

    @pytest.mark.skip("to be implemented afterwards")
    def test_user_authentication(self):
        """Tests login and logout"""
        json_data = request.get_json()
        email = json_data['email']
        password = json_data['password']
        return jsonify(token={email, password})

        with self.client() as c:
            rv = c.post('/api/auth', json={
            'username': 'flask', 'password': 'secret'
            })
            json_data = rv.get_json()
        assert(json_data['email'], json_data['token'])
    
    
    def test_api_can_get_all_users(self):
        """Test api Get all the users"""
        response = self.client().get('/api/v1/user/')
        self.assertTrue(response.status_code, 200)
        

    def test_api_can_get_users_by_id(self):
        """Test api can get a users by id"""
        rv = self.client().post('/api/v1/user/', 
                data = json.dumps(dict(self.req)))
        self.assertEquals(rv.status_code, 201)

        res = self.client().get('/api/v1/user/3')
        self.assertEquals(res.status_code, 200)

    def test_api_users_can_be_modified(self):
        #Test api can modify a users
        rv = self.client().post('/api/v1/user/', 
                data = json.dumps(dict(self.req)))
        self.assertEquals(rv.status_code, 201)

        res = self.client().put('/api/v1/user/3',
                data = json.dumps(dict(self.modified)))
        self.assertEquals(res.status_code, 201)
        self.assertIn('susansue@gmail.com', str(res.data))

    def test_api_can_create_users(self):
        """Test api can create a users"""
        res = self.client().post('/api/v1/user/', data = json.dumps(dict(self.req)))
        self.assertEquals(res.status_code, 201)
        self.assertIn('mary', str(res.data))

    def test_api_can_delete_user(self):
        rv = self.client().post('/api/v1/user/', 
                data = json.dumps(dict({"email":"sue@gmail.com"})))
        self.assertEquals(rv.status_code, 200)

        res = self.client().delete('/api/v1/user/1')
        self.assertEquals(res.status_code, 201)

        res = self.client().get('/api/v1/user/1')
        self.assertEquals(res.status_code, 404)