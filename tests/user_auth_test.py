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
        self.app = create_app(TestingConfig.TESTING)
        self.client = self.app.test_client
        self.ctx = self.app.test_request_context
        

    @pytest.mark.skip("to be implemented afterwards")
    def test_user_authentication(self):
        """Tests login and logout"""
        json_data = request.get_json()
        email = json_data['email']
        password = json_data['password']
        return jsonify(token={email, password})

        with create_app(TestingConfig.TESTING).test_client() as c:
            rv = c.post('/api/auth', json={
            'username': 'flask', 'password': 'secret'
            })
            json_data = rv.get_json()
        assert(json_data['email'], json_data['token'])