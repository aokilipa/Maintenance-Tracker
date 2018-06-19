"""
incomplete
implemented using data structures
#creating dtrequest, dtuser and dtlogin list with dictionary 
 to simulate data store

"""

import psycopg2
from datetime import datetime
from config import dbconfig, basedir, filename , section, DATABASE_URL
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

def is_admin(username):
    #check if user is admin
    query = """SELECT username from tb_users WHERE username=(%s) AND role=True"""
    
    conn = None
    result = None
    try:
        params = dbconfig(filename, section)

        conn = psycopg2.connect(**params)

        
        cur = conn.cursor()

        cur.execute(query, (username,))

        result = cur.fetchall()

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        return "iko shida " + str(error)
    
    finally:
        if conn is not None:
            conn.close()
    
    if result is None:
        return False

    return True

def fetch_all_request():
        """get all request"""
        query = """select array_to_json(array_agg(row_to_json(t))) from
                (SELECT * from tb_request) t"""
        
        conn = None
        results = None
        try:
            conn=psycopg2.connect(DATABASE_URL())
            cur = conn.cursor()

            cur.execute(query)
            results = cur.fetchall()

            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            return error
        finally:
            if conn is not None:
                conn.close()
        
        return results

def fetch_for_logged_in_user(requestor):
        """get all request for logged in user"""
        query = """select row_to_json(t) from (
                    select * from tb_request WHERE requestor=(%s)) t"""
        
        conn = None
        results = None
        try:
            conn=psycopg2.connect(DATABASE_URL())
            cur = conn.cursor()

            cur.execute(query,(requestor,))
            results = cur.fetchall()

            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            return error
        finally:
            if conn is not None:
                conn.close()
        
        return results

current_user = find_by_username("antokish@gmail.com")
result = fetch_all_request()

if __name__ == '__main__':
    #test_connection()
    #current_user[0]
    print(fetch_for_logged_in_user(2))
    #print(result)

    
    