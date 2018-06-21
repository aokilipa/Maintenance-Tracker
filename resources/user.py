"""
from flask import Flask, jsonify, request, abort, g
from flask_restful import Api,Resource, reqparse
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pass_context


from flask_jwt_extended import (create_access_token,create_refresh_token,
jwt_required, jwt_refresh_token_required,get_jwt_identity, get_raw_jwt)

auth = HTTPBasicAuth()

#parsing incoming data
parser = reqparse.RequestParser()
parser.add_argument('username', help = 'Please fill in the username', required = True)
parser.add_argument('password', help= 'This field cannot be blank', required = True)
class UserResource(Resource):
    #get all registered users
    def get(self):
        return dtusers, 200

    #create new user
    def post(self):
        #json_data = request.get_json(force=True)
        data = parser.parse_args()        
    
        
        try:
            dtusers.append(data)
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity = data['username'])

            return {
                'message': 'User {} was created'.format(data['username']),
                'access_token': access_token,
                'refresh_token': refresh_token
            }

        except:
            return {'message':'Somenthing went wrong'}, 500

        return {"status":"success", "data": data }, 201
    

class User(Resource):
    #get user by id
    def get(self, uid):
        for user in dtusers:
            if (uid== user['id']):
                return user, 200    
        return "No record found", 404
    
    #Modify / update an existing user
    def put(self, uid):
        json_data = request.get_json(force=True)
        for user in dtusers:
            if (uid == user['id']):
                user.update(json_data)
                return {"status":"success", "data": json_data }, 201
        return "Request not found", 404
    
    #Delete user
    def delete(self, uid):
        for user in dtusers:
            if (uid == user['id']):
                dtusers[:]=[user for user in dtusers if not(uid == user.get('id'))]
                return {"status":"Deleted successfuly", "data": user}, 201
        return "Record not found", 404
"""