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
import flask

from app import api_bp
from resources.requests import dtrequest, RequestResource, Request
from run import create_app
from config import app_config


@pytest.mark.unittest
class ApiTest(unittest.TestCase):
    """ API endpoints test case"""

    def setUp(self):
        """Declare test variables and initialize app."""
        self.app = create_app(config_filename=app_config['testing'])
        self.client = self.app.test_client
        self.data = {"id": 1, "requestor":"Alicia Keys", "type": "maintenance",
        "status":"Approved", "desc": "Description goes here"}
    
    def tearDown(self):
        pass
        

        

    def test_api_can_get_all_requests(self):
        """Test api Get all the requests for a logged in user"""
        result = RequestResource.get(self)
        res = result[0]
        self.assertEquals(res, dtrequest)
        

    def test_api_can_get_request_by_id(self):
        """Test api can get a request for a logged in user"""
        result = Request.get(self, 1)
        res = result[0]
        self.assertEquals(res['id'], 1)

    @pytest.mark.skip()
    def test_api_request_can_be_modified(self):
        """Test api can modify a request"""
        result = self.client.put() #Request.put(self,1)
        self.assertEquals(res['status'], 'Resolved')

    def test_api_can_create_request(self):
        """Test api can create a request"""
        pass
        

#Make tests executable
if __name__ == "__main__":
    unittest.main()