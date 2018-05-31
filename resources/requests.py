from flask_restful import Resource, reqparse
from flask import json, request

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
        return dtrequest, 200

    """create new request"""
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        dtrequest.append(json_data)
        return {"status":"success", "data": json_data }, 201
        
    
    
class Request(Resource):
    """Get request by ID"""
    def get(self, req_id):
        for _request in dtrequest:
            if (req_id == _request['id']):
                return _request, 200
        return "request not found", 404
    
    """Modify a request"""
    def put(self, req_id):
        json_data = request.get_json(force=True)
        for _request in dtrequest:
            if (req_id == _request['id']):
                _request.update(json_data)
                return {"status":"success", "data": json_data }, 201
        return "Request not found", 404