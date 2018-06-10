import os
import unittest
import pytest
import psycopg2

from flask import json, request, jsonify
from run import create_app
from tests.models import create_tables

@pytest.mark.unittest

class AuthTest(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client
        self.reg = { "username": "mary@gmail.com", "firstname": "Mary", 
                    "lastname": "Doe","password": "Doe","created_on": "Doe" }


        with self.app.app_context():
            create_tables()

    def tearDown(self):
        pass
    

    def test_encode_auth_token(self):
       """ 
       user = UserAuth(
            email = 'test@gmail.com',
            password = 'test'
        )
        auth_token = user.encode_auth_token(user.id)
        """

    @pytest.mark.skip("to run after implementation")
    def test_registration_endpoint(self):
        """Test signup/register users endpoint"""
        res = self.client().post('/api/v1/auth/signup/', data = json.dumps(dict(self.reg)))
        self.assertEquals(res.status_code, 201)
        self.assertIn('mary', str(res.data))
    
    @pytest.mark.skip("to run after implementation")
    def test_login_endpoint(self):
        """Test login endpoint"""
        res = self.client().post('/api/v1/auth/login/', data = json.dumps(dict(self.reg)))
        self.assertEquals(res.status_code,201)
        
    @pytest.mark.skip("to run after implementation")
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