import pytest
import unittest

@pytest.mark.usefixtures("requests")
class ApiTest(unittest.TestCase):
    """ API endpoints test case"""

    def test_api_can_get_all_requests(self):
        """Test api Get all the requests for a logged in user"""
        res = self.client().post('/api/', requests)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/api')
        self.assertEqual(res.status_code, 200)
        self.assertIn("John doe")

    def test_api_can_get_request_by_id(self):
        """Test api can get a request for a logged in user"""
        res = self.client().post('/api/', requests)
        self.assertEqual(res.status_code, 201)
        json_res = json.loads(.data.decode('utf-8').replace("'", "\""))
        result = self.client().get(
            '/api/{}'.format(json_res['id']))
        self.assertEqual(result.status_code, 200)
        self.assertIn("John doe")

    def test_api_request_can_be_modified(self):
        """Test api can modify a request"""
        res = self.client().post('api', data={"user":"john doe"})
        res = self.client().put('/api/1', data ={"user":"John sue doe"})
        self.assertEqual(res.status_code, 200)
        results = self.client().get('/api/1')
        self.assertIn('sue', str(requests))


    def test_api_can_create_request(self):
        """Test api can create a request"""
        res = self.client().post('/api/', data=requests)
        self.assertEqual(res.status_code, 201)
        self.assertIn('John doe', str(res.data))

#Make tests executable
if __name__ == "__main__":
    unittest.main()
