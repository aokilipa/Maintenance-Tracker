from flask_restful import Resource, reqparse
from flask import json, request, jsonify
from models import dtrequest



class RequestResource(Resource):
    
    """Get all request"""
    def get(self):    
        #to set in utils
        current_user = ["anto@gmail.com"]
        res = [d for d in dtrequest if d["email"] in current_user]
        return res

    """create new request"""
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        elif (len(json_data)!=len(dtrequest[0])):
            return "Please enter all details"
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