import os
import unittest
import pytest
import psycopg2

from flask import json, request, jsonify
from run import create_app
from resources.models import find_by_username, return_all, insert_to_db


@pytest.mark.unittest

class AuthTest(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.reg =  { "username": "anto@gmail.com", "password": "test", "firstname": "antony",
 	                    "lastname": "okilipa","role":"yes" }
        self.login_data = { "username": "anto@gmail.com",
                            "password": "test"
                            }

        #with self.app.app_context():
           

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

    
    def test_registration_endpoint(self):
        """Test signup/register users endpoint"""
        res = self.client().post('/api/v1/auth/signup', data = self.reg)
        self.assertEquals(res.status_code, 200)
        self.assertIn('anto@gmail.com', str(res.data))
    

    def test_login_endpoint(self):
        """Test login endpoint"""
        res = self.client().post('/api/v1/auth/login', 
                                data = json.dumps(dict({ 
                                    "username": "anto@gmail.com",
                                    "password": "test"
                            })))
        self.assertEquals(res.status_code,200)
        self.assertIn('anto@gmail.com',str(res.data))

    def test_logout_access(self):
        pass
    
    def test_logout_refresh(self):
        res = self.client().post('/api/v1/auth/logout/refresh')
        self.assertEquals(res.status_code, 200)
    
    def test_token_refresh(self):
        res = self.client().post('/api/v1/auth/token/refresh')
        self.assertEquals(res.status_code, 200)