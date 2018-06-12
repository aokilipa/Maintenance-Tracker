"""
incomplete
implemented using data structures
#creating dtrequest, dtuser and dtlogin list with dictionary 
 to simulate data store

"""

import psycopg2
from config import dbconfig, basedir, filename , section
import os
import jwt

from flask import json, jsonify
from itsdangerous import (TimedJSONWebSignatureSerializer 
                            as Serializer, BadSignature, SignatureExpired)





def test_connection():
    """Test connection to the postgresql server"""

    conn = None
    try:
        #read conection parameters
        params =  dbconfig(filename,section)
        
        #connect to server
        print('Conecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        #create a cursor
        cur = conn.cursor()

        #execute a statement
        print('Postgres database version: ')
        cur.execute('SELECT version()')

        #display the postgress db server version
        db_version = cur.fetchone()
        print(db_version)

        #close comm with pgSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')






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
def find_by_username(username):
    query = """SELECT username,password FROM tb_users WHERE username=(%s)"""
    
    conn = None
    result = None
    try:
        params = dbconfig(filename, section)
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        cur.execute(query,(username,))

        result = cur.fetchone()
        
        #print(result)
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return result

def return_all():
    query = """select array_to_json(array_agg(row_to_json(t))) from (  
                SELECT * FROM tb_users) t"""
    
    conn = None
    result = None

    try:
        params = dbconfig(filename, section)

        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        cur.execute(query)

        result = cur.fetchall()

        cur.close()


    except (Exception, psycopg2.DatabaseError) as error:
        print (error)
    finally:
        if conn is not None:
            conn.close()
    return result

current_user = find_by_username("antokish@gmail.com")

if __name__ == '__main__':
    #test_connection()
    current_user[0]
    print(return_all())