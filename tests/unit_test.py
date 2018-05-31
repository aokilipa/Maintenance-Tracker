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

@pytest.mark.usefixtures("requests")
class ApiTest(unittest.TestCase):
    """ API endpoints test case"""

    def test_api_can_get_all_requests(self):
        """Test api Get all the requests for a logged in user"""
        res = self.client().post('/api/v1/user/requests/', requests)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/api/v1/user/requests')
        self.assertEqual(res.status_code, 200)
        self.assertIn("John doe", str(res))

    def test_api_can_get_request_by_id(self):
        """Test api can get a request for a logged in user"""
        res = self.client().post('/api/v1/user/requests/', requests)
        self.assertEqual(res.status_code, 201)
        json_res = json.loads()
        result = self.client().get(
            '/api/v1/user/requests{}'.format(json_res['id']))
        self.assertEqual(result.status_code, 200)
        self.assertIn("John doe")

    def test_api_request_can_be_modified(self):
        """Test api can modify a request"""
        res = self.client().post('/api/v1/user/requests/', data={"user":"john doe"})
        res = self.client().put('/api/v1/user/requests/1', data ={"user":"John sue doe"})
        self.assertEqual(res.status_code, 200)
        results = self.client().get('/api/v1/user/requests/1')
        self.assertIn('sue', str(requests))


    def test_api_can_create_request(self):
        """Test api can create a request"""
        res = self.client().post('/api/v1/user/requests/', data=requests)
        self.assertEqual(res.status_code, 201)
        self.assertIn('John doe', str(res.data))

#Make tests executable
if __name__ == "__main__":
    unittest.main()