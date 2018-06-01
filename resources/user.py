from flask import Flask, jsonify, request
from flask_restful import Api,Resource, reqparse

dtusers = [
    {
        "id": 1,
        "fname": "John", 
        "lname": "Doe",
        "email": "john@gmail.com", 
        "username": "john@gmail.com" 
    },
    {
        "id": 2,
        "fname": "Susan", 
        "lname": "Sue",
        "email": "john@gmail.com", 
        "username": "john@gmail.com" 
    },
    {
        "id": 3,
        "fname": "Mary", 
        "lname": "Doe",
        "email": "john@gmail.com", 
        "username": "john@gmail.com" 
    },
    {
        "id": 4,
        "fname": "Anto", 
        "lname": "Denis",
        "email": "john@gmail.com", 
        "username": "john@gmail.com" 
    }
]

class UserResource(Resource):
    """get all registered users"""
    def get(self):
        return dtusers, 200

    """create new user"""
    def post(self):
        json_data = request.get_json(force=True)
        
        if not json_data:
            return {'message': 'No input data provided'}, 400
        elif (len(json_data)!=len(dtusers[0])):
            return "Please enter all details"
        
        dtusers.append(json_data)
        return {"status":"success", "data": json_data }, 201
    

class User(Resource):
    """get user by id"""
    def get(self, uid):
        for user in dtusers:
            if (uid== user['id']):
                return user, 200    
        return "No record found", 404
    
    """Modify / update an existing user"""
    def put(self, uid):
        json_data = request.get_json(force=True)
        for user in dtusers:
            if (uid == user['id']):
                user.update(json_data)
                return {"status":"success", "data": json_data }, 201
        return "Request not found", 404
    
    """Delete user"""
    def delete(self, uid):
        for user in dtusers:
            if (uid == user['id']):
                dtusers[:]=[user for user in dtusers if not(uid == user.get('id'))]
                return {"status":"Deleted successfuly", "data": user}, 201
        return "Record not found", 404
        
            