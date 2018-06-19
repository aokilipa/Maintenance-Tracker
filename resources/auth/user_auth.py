import os
import json
from datetime import datetime


from flask import Flask, abort, request , jsonify, g, json
from flask_restful import Api, Resource, reqparse
from resources.models import (insert_to_db, find_by_username, hash_password, verify_hash,
                            return_all)

from flask_jwt_extended import (create_access_token,create_refresh_token,
jwt_required, jwt_refresh_token_required,get_jwt_identity, get_raw_jwt)



#parsing incoming data
parser = reqparse.RequestParser()
parser.add_argument('username', help = 'Please fill in the username', required = True)
parser.add_argument('password', help= 'This field cannot be blank', required = True)

class UserSignup(Resource):
    
      
    #register user
    def post(self):
        #parser.add_argument('firstname', help = 'This field cannot be blank', required = True)
        parser.add_argument('firstname', help = 'This field cannot be blank', required = True)
        parser.add_argument('lastname', help = 'This field cannot be blank', required = True)
        parser.add_argument('role',help = 'if admin', required = False)

        self.data = parser.parse_args()

        username = self.data['username']
        password = hash_password(self.data['password']) 
        firstname = self.data['firstname']
        lastname = self.data['lastname']
        role = self.data['role']
        created_on = datetime.now()
        
        current_user = find_by_username(username)

        
        if current_user is None:
            pass
        elif current_user[1]==username:
            return{"message":"user {} already exist".format(username)}
        
        try:
            
            insert_to_db(self, username, password, firstname,lastname,role, created_on)
            
            access_token = create_access_token(identity=username)
            refresh_token = create_refresh_token(identity=username)

            return{
                "message":"User {} was created".format(username),
                "access_token": access_token,
                "refresh_token": refresh_token
            }

        except:
            return{"message":"error registering user"}
        
        
        return{"data":self.data}

class UserLogin(Resource):

   
    #login user
    def post(self):
        self.data = parser.parse_args()

        username = self.data['username']
        password = self.data['password']

        current_user = find_by_username(username)

        if current_user is None:
            return {"message": "user {} doesn\'t exist".format(username)}
        
        if verify_hash(password, current_user[2]):
            access_token = create_access_token(identity=username)
            refresh_token = create_refresh_token(identity=username)
            return {
                "message": "Logged in as {}".format(username),
                "access_token": access_token,
                "refresh_token": refresh_token
                }
        else:
            return {"message":"Wrong credentials"}


class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            return {'message':'Logged out succesfuly'}
        except:
            return {'message':'Something went wrong'}, 500
        

class UserLogoutRefresh(Resource):
    def post(self):
        return {'message':'Logout Refresh'}

class TokenRefresh(Resource):
    """reissue access token with refresh token"""
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity = current_user)
        return {'access_token':access_token}

class AllUsers(Resource):
    #get all registered users
    @jwt_required
    def get(self):
        return return_all()
    
    def delete(self):
        pass