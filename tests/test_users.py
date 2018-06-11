import unittest
import json
import os
import pytest

from config import TestingConfig
from run import create_app
from resources.user import User, UserResource
from flask import request, jsonify

@pytest.mark.unittest
class UserTest(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client
        self.ctx = self.app.test_request_context
        self.req = {  "id": 4,"fname": "Mary", "lname": "Doe", "username": "mary@gmail.com","password":"test" }
        self.modified = {  "id": 3,"fname": "Mary", "lname": "Doe", "email": "susansue@gmail.com" }
        
    
    
    def test_api_can_get_all_users(self):
        """Test api Get all the users"""
        response = self.client().get('/api/v1/user/')
        self.assertTrue(response.status_code, 200)
        

    def test_api_can_get_users_by_id(self):
        """Test api can get a users by id"""
        rv = self.client().post('/api/v1/user/', 
                data = self.req)

        res = self.client().get('/api/v1/user/3')
        self.assertEquals(res.status_code, 200)

    def test_api_users_can_be_modified(self):
        #Test api can modify a users

        res = self.client().put('/api/v1/user/3',
                data = json.dumps(dict(self.modified)))
        self.assertEquals(res.status_code, 201)
        self.assertIn('susansue@gmail.com', str(res.data))

    def test_api_can_create_users(self):
        """Test api can create a users"""
        res = self.client().post('/api/v1/user/', data = self.req)
        self.assertEquals(res.status_code, 200)
        self.assertIn('mary', str(res.data))

    def test_api_can_delete_user(self):

        res = self.client().delete('/api/v1/user/1')
        self.assertEquals(res.status_code, 201)