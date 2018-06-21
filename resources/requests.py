import datetime

from flask_restful import Resource, reqparse
from flask import json, request, jsonify
from resources.models import RequestModel, is_admin, find_by_username

from flask_jwt_extended import (create_access_token,create_refresh_token,
jwt_required, jwt_refresh_token_required,get_jwt_identity, get_raw_jwt)

#set current user


RM = RequestModel

parser = reqparse.RequestParser()
parser.add_argument('requestor',help='fill user id', required=True)
parser.add_argument('request_type',help='please fill in request_type', required=True)
parser.add_argument('status',help='request status', required=False)
parser.add_argument('description',help='please fill in descritption', required=True)

class RequestResource(Resource):
    
    """Get all request"""
    @jwt_required
    def get(self):    
        
        current_user = get_jwt_identity()
        user_id = find_by_username(current_user)[0]
        check_admin = is_admin(current_user)
        if  check_admin is True:
            """returns all request"""
            return RM.fetch_all_request()
        return {current_user:RM.fetch_for_logged_in_user(user_id)}

    @jwt_required
    def post(self):
        """create new request"""
        self.data = parser.parse_args()

        requestor = self.data['requestor']
        request_type = self.data['request_type']
        status = self.data['status']
        description = self.data['description']
        created_on = datetime.datetime.now()

        try:
            save = RequestModel.create_request(self,requestor,request_type,status,description,created_on)
            
            return {"status":str(save), "data": request_type }, 201
        
        except:
            return {"msg":"Failed to create new request"}
        
        #return {"status":"success", "data": self.data }, 201
        
    
    
class Request(Resource):
    """Get request by ID"""
    @jwt_required
    def get(self, req_id):
        response = RM.fetch_request_by_id(self, req_id)[0][0]
        current_user = get_jwt_identity()
        user_id = find_by_username(current_user)[0]

        if user_id == response['requestor']:
            return response
        return {"msg": "You have insufficient rights to view this"}
    
    @jwt_required
    def put(self, req_id):
        """Modify a request"""
        json_data = request.get_json(force=True)
        request_type=json_data['request_type']
        description=json_data['description']
        last_modified=datetime.datetime.now()
        request_id = req_id

        try:
            RM.modify_request(request_type,description,last_modified,request_id)

            return {"message":"Record updated succesfully"}
        except:
            return {"message":"failed to update request"}
    
    def delete(self):
        pass
    
class GetAllRequest(Resource):
    """Fetch all request Admin only"""
    @jwt_required
    def get(self):
        current_user = get_jwt_identity()
        check_admin = is_admin(current_user)

        if check_admin is True:
            return RM.fetch_all_request()[0][0]
        return {"message":"you dont have sufficient rights to access this"}

class ApproveRequest(Resource):
    """Approve user request"""
    @jwt_required
    def put(self, req_id):
        """Modify a request"""
        json_data = request.get_json(force=True)
        status=json_data['status']
        last_modified=datetime.datetime.now()
        request_id = req_id

        current_user = get_jwt_identity()
        check_admin = is_admin(current_user)
        
        if check_admin is True:
            try:
                RM.request_action(self, status,last_modified,request_id)

                return {"message":"request {} {}".format(request_id, status)}
            except:
                return {"message":"failed to approve request"}
        
        return {"message":"you dont have sufficient rights to access this"}

class DisapproveRequest(Resource):
    """Dissapprove user request"""
    @jwt_required
    def put(self, req_id):
        """Modify a request"""
        json_data = request.get_json(force=True)
        status=json_data['status']
        last_modified=datetime.datetime.now()
        request_id = req_id
        
        current_user = get_jwt_identity()
        check_admin = is_admin(current_user)

        if check_admin is True:
            try:
                RM.request_action(self, status,last_modified,request_id)

                return {"message":"request {} {}".format(request_id, status)}
            except:
                return {"message":"failed to approve request"}
        
        return {"message":"you dont have sufficient rights to access this"}

class ResolveRequest(Resource):
    """Resolve user request"""
    @jwt_required
    def put(self, req_id):
        """Modify a request"""
        json_data = request.get_json(force=True)
        status=json_data['status']
        last_modified=datetime.datetime.now()
        request_id = req_id
        
        current_user = get_jwt_identity()
        check_admin = is_admin(current_user)

        if check_admin is True:
            try:
                
                RM.request_action(self, status,last_modified,request_id)

                return {"message":"request {} {}".format(request_id, status)}
            except:
                return {"message":"failed to approve request"}
        
        return {"message":"you dont have sufficient rights to access this"}