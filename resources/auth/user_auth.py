import os
import json

from flask import Flask, abort, request , jsonify, g, json
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource
from models import UserAuth, dtlogin

auth = HTTPBasicAuth
app = Flask(__name__)
class UserAuthResouce(Resource):
    
    @auth.verify_password
    def verify_password(self):
        pass
    
    #route('/api/v1/register')
    def create_user(self):
        json_data = request.get_json(force = True)
        username = request.json.get('username')
        password = request.json.get('password')
        if username is None or password is None:
            abort(400)
        for user in dtlogin:
            if (username==user['username']):
                abort(400) #usr exists
        user = username
        dtlogin.append(json_data)
        return {"status":"success", "data": json_data }, 201
    
    #route('/api/v1/register/<int:id>')
    def get_user(self, uid):
        for user in dtlogin:
            if (uid== user['id']):
                return user, 200    
        return "No record found", 404
    
    #route('/api/v1/token')
    @auth.login_required
    def get_auth_token(self):
        token = g.UserAuth.generate_auth_token(600)
        return jsonify({'token': token.decode('ascii'), 'duration': 600})
    
    #route('/api/v1/register/<int:id>')
    @auth.login_required
    def get_resource(self):
        return jsonify({'data': 'Hello, %s!' % g.user.username})