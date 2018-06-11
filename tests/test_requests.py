"""
APIs endpoint test
test:
    -> gets all the requests for logged in user
    -> gets a request for a logged in user
    -> creates a request
    -> Modify a request

"""

import unittest
import json
import os
import pytest

from flask_restful import Api
from resources.requests import dtrequest, RequestResource, Request
from run import create_app
from app import api_bp


@pytest.mark.unittest
class ApiTest(unittest.TestCase):
    """ API endpoints test case"""

    def setUp(self):
        #Declare test variables and initialize app
        self.app = create_app('testing')
        self.client = self.app.test_client
        self.req = { "id": 5, "requestor":"Test Doe", "email": "john@gmail.com",
                "type": "maintenance", "status":"Approved", "desc": "Description goes here"}
       
        
           
    def tearDown(self):
        pass
        

        

    def test_api_can_get_all_requests(self):
        """Test api Get all the requests for a logged in user"""
        response = self.client().get('/api/v1/user/request')
        self.assertTrue(response.status_code, 200)
        

    def test_api_can_get_request_by_id(self):
        """Test api can get a request for a logged in user"""
        res = self.client().get('/api/v1/user/request/1')
        self.assertEquals(res.status_code, 200)

    def test_api_request_can_be_modified(self):
        #Test api can modify a request
        rv = self.client().post('/api/v1/user/request/', 
                data = json.dumps(dict({"requestor":"sue doe"})))
        self.assertEquals(rv.status_code, 200)

        res = self.client().put('/api/v1/user/request/1',
                data = json.dumps(dict({"requestor":"Susan Sue"})))
        self.assertEquals(rv.status_code, 200)
        self.assertIn('Susan Sue', str(res.data))


    def test_api_can_create_request(self):
        """Test api can create a request"""
        res = self.client().post('/api/v1/user/request/', data = json.dumps(dict(self.req)))
        self.assertEquals(res.status_code, 201)
        self.assertIn('Test Doe', str(res.data))
        

#Make tests executable
if __name__ == "__main__":
    unittest.main()