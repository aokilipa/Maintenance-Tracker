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

from resources.User_request import dtrequest
from run import create_app
import config


@pytest.mark.unittest
class ApiTest(unittest.TestCase):
    """ API endpoints test case"""

    def setUp(self):
        """Declare test variables and initialize app."""
        self.app = create_app(config_filename="testing")
        self.client = self.app.test_client
        self.status = {'status': 'Active'}

        

    def test_api_can_get_all_requests(self):
        """Test api Get all the requests for a logged in user"""
        res = self.client().post('/api/v1/user/requests/', dtrequest)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/api/v1/user/requests')
        self.assertEqual(res.status_code, 200)
        self.assertIn("John doe", str(res))

    def test_api_can_get_request_by_id(self):
        """Test api can get a request for a logged in user"""
        res = self.client().post('/api/v1/user/requests/', dtrequest)
        self.assertEqual(res.status_code, 201)
        json_res = json.loads(dtrequest)
        result = self.client().get(
            '/api/v1/user/requests{}'.format(json_res['status']))
        self.assertEqual(result.status_code, 200)
        self.assertIn("Resolved", dtrequest)

    def test_api_request_can_be_modified(self):
        """Test api can modify a request"""
        res = self.client().post('/api/v1/user/requests/1', data={"status":"Approved"})
        res = self.client().put('/api/v1/user/requests/1', data ={"user":"Resolved"})
        self.assertEqual(res.status_code, 200)
        results = self.client().get('/api/v1/user/requests/1')
        self.assertIn('resolved', str(results.object))


    def test_api_can_create_request(self):
        """Test api can create a request"""
        res = self.client().post('/api/v1/user/requests/', data=dtrequest)
        self.assertEqual(res.status_code, 201)
        self.assertIn('John doe', str(res.data))

#Make tests executable
if __name__ == "__main__":
    unittest.main()