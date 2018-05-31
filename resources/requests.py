from flask_restful import Resource
from flask import jsonify

#creating dtrequest list with dictionary to simulate data store
#using datastructure to simulate data store
dtrequest = [
    {
        "id": 1,
        "requestor":"Alicia Keys",
        "type": "maintenance",
        "status":"Approved",
        "desc": "Description goes here"
    },
    {
        "id": 2,
        "requestor":"John Doe",
        "type": "repair",
        "status":"Pending",
        "desc": "Description goes here"
    },
    {
        "id": 3,
        "requestor":"Susan Doe",
        "type": "maintenance",
        "status":"Approved",
        "desc": "Description goes here"
    },
    {
        "id": 4,
        "requestor":"John Doe",
        "type": "maintenance",
        "status":"Approved",
        "desc": "Description goes here"
    }
]

class RequestResource(Resource):
    """Get all request"""
    def get(self):     
        return dtrequest
    
    
class Request(Resource):
    """Get request by ID"""
    def get(self, req_id):
        for request in dtrequest:
            if (req_id == request['id']):
                return request, 200
        return "request not found", 404