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

from run import create_app


@pytest.mark.unittest
class ApiTest(unittest.TestCase):
    """ API endpoints test case"""

    def setUp(self):
        #Declare test variables and initialize app
        self.app = create_app('testing')
        self.client = self.app.test_client
        self.req ={
            "requestor":1,
	        "request_type": "Repair",
	        "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quasi ipsam possimus cumque libero ipsa vero odio.",
	        "status":"Pending"
            }
    def signup(self):
        user_details ={
 	        'username': "anto@mail.com",
 	        'password': "test",
 	        'firstname': "anto",
 	        'lastname': "Doe",
 	        'role': "t"
            }
        return self.client().post('/api/v1/auth/signup', data=user_details)
	
    def login(self):
        login_details = {
            "username":"anto@mail.com",
            "password":"test"
        }
        return self.client().post('/api/v1/auth/login', 
                                data=json.dumps(dict(login_details)))
           
    def tearDown(self):
        pass
        

        

    def test_api_can_get_all_requests(self):
        """Test api Get all the requests for a logged in user"""
        self.signup()
        res = self.login()
        access_token = json.loads(res.data.decode())['access_token']
        response = self.client().get('/api/v1/users/requests',
                        headers=dict(Authorization="Bearer "+ access_token))
        self.assertTrue(response.status_code, 200)
        
        

    def test_api_can_get_request_by_id(self):
        """Test api can get a request for a logged in user"""
        self.signup()
        res = self.login()
        access_token = json.loads(res.data.decode())['access_token']
        res = self.client().get('/api/v1/users/requests/1',
                                headers=dict(Authorization="Bearer "+ access_token))
        self.assertEquals(res.status_code, 200)

    def test_api_request_can_be_modified(self):
        #Test api can modify a request
        self.signup()
        res = self.login()
        
        access_token = json.loads(res.data.decode())['access_token']

        rv = self.client().post('/api/v1/users/requests/',
                headers=dict(Authorization="Bearer "+ access_token), 
                data = self.req)
        self.assertEquals(rv.status_code, 201)

        res = self.client().put('/api/v1/users/requests/1',
                headers=dict(Authorization="Bearer "+ access_token),
                data = json.dumps(dict({"request_type":"repair", "description":"This is an updated description"})))
        self.assertEquals(rv.status_code, 201)
        self.assertIn('Record updated succesfully', str(res.data))


    def test_api_can_create_request(self):
        """Test api can create a request"""
        self.signup()
        result = self.login()
        access_token = json.loads(result.data.decode())['access_token']

        res = self.client().post(
            '/api/v1/users/requests/',
            headers=dict(Authorization="Bearer " + access_token), 
            data = self.req)
        self.assertEquals(res.status_code, 201)
        self.assertIn('Data saved succesfully', str(res.data))
        

#Make tests executable
if __name__ == "__main__":
    unittest.main()