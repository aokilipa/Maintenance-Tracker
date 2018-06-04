"""
incomplete
implemented using data structures
#creating dtrequest, dtuser and dtlogin list with dictionary 
 to simulate data store

"""

from flask import json, jsonify
from itsdangerous import (TimedJSONWebSignatureSerializer 
                            as Serializer, BadSignature, SignatureExpired)

#User sample data
dtusers = [
{
        "id": 1,
        "fname": "John", 
        "lname": "Doe",
        "email": "john@gmail.com"  
    },
    {
        "id": 2,
        "fname": "Susan", 
        "lname": "Sue",
        "email": "sue@gmail.com" 
    },
    {
        "id": 3,
        "fname": "Mary", 
        "lname": "Doe",
        "email": "mary@gmail.com" 
    },
    {
        "id": 4,
        "fname": "Anto", 
        "lname": "Denis",
        "email": "anto@gmail.com"
    }
]

#requests sample data
dtrequest = [
    {
        "id": 1,
        "requestor":"Anto kish",
        "email": "anto@gmail.com",
        "type": "maintenance",
        "status":"Approved",
        "desc": "Description goes here"
    },
    {
        "id": 2,
        "requestor":"John Doe",
        "email": "john@gmail.com",
        "type": "repair",
        "status":"Pending",
        "desc": "Description goes here"
    },
    {
        "id": 3,
        "requestor":"Anto kish",
        "email": "anto@gmail.com",
        "type": "maintenance",
        "status":"Pending",
        "desc": "Description goes here"
    },
    {
        "id": 4,
        "requestor":"John Doe",
        "email": "john@gmail.com",
        "type": "maintenance",
        "status":"Approved",
        "desc": "Description goes here"
    }
]
#login data
dtlogin = [
    {
        "id": 1,
        "username": "john@gmail.com",
        "password": "pass"
    },
    {
        "id": 2,
        "username": "sue@gmail.com",
        "password": "pass"
    }

]

"""To be implemented when intergrating with database"""
class UserAuth(object):
    def hash_password(self, pwd):
        pass

    def verify_password(self, pwd):
        pass

    def generate_auth_token(self, expiration=600):
        pass

    @staticmethod
    def verify_auth_token(token):
        pass