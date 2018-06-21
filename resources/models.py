from flask import Flask
import datetime
import psycopg2

from passlib.hash import pbkdf2_sha256 as sha256
from run import create_app
from config import dbconfig, filename ,section, app_config, DATABASE_URL
from flask_bcrypt import Bcrypt

app = Flask(__name__)

def insert_to_db(self, username, password, firstname, lastname, role, created_on):
    """insert a new user into database"""

    query = """INSERT INTO tb_users (username, password, firstname, lastname,role, created_on)
                VALUES(%s,%s,%s,%s,%s,%s)"""
    
    conn = None
    user_id = None
    try:
        #params = dbconfig(filename, section)
        conn = psycopg2.connect(DATABASE_URL())

        cur = conn.cursor()
        cur.execute(query,(username, password, firstname, 
                    lastname,role, created_on,))

               
        conn.commit()
        user_id = cur.fetchone()[0]
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        return error
    finally:
        if conn is not None:
            conn.close()
    return user_id

def find_by_username(username):
    query = """SELECT user_id,username,password FROM tb_users WHERE username=(%s)"""
    
    conn = None
    result = None
    try:
        #params = dbconfig(filename, section)
        conn = psycopg2.connect(DATABASE_URL())

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
        #params = dbconfig(filename, section)

        conn = psycopg2.connect(DATABASE_URL())

        cur = conn.cursor()
        cur.execute(query)

        result = cur.fetchall()

        cur.close()


    except (Exception, psycopg2.DatabaseError) as error:
        return str(error)
    finally:
        if conn is not None:
            conn.close()
    return result


def hash_password(password):
    #generate hashed string to store in db
    return sha256.hash(password)


def verify_hash(password, hash):
    #check the given pass
    return sha256.verify(password, hash)

def is_admin(username):
    #check if user is admin
    query = """SELECT username from tb_users WHERE username=(%s) AND role=True"""
    
    conn = None
    result = None
    try:
        conn = psycopg2.connect(DATABASE_URL())
        
        cur = conn.cursor()

        cur.execute(query, (username,))

        result = cur.fetchone()

        cur.close()

        if result is None or result == "":
            return False

    except (Exception, psycopg2.DatabaseError) as error:
        return "iko shida " + str(error)
    
    finally:
        if conn is not None:
            conn.close()

    return True

def get_id(username):
    pass

class RevokedTokenModel(object):
    pass

class RequestModel(object):
    def fetch_all_request():
        """get all request"""
        query = """select array_to_json(array_agg(row_to_json(t))) from (
                    select * from tb_request) t"""
        
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
        query = """select array_to_json(array_agg(row_to_json(t))) from (
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
    
    def fetch_request_by_id(self, request_id):
        """get a request for a logged in user"""
        query = """select row_to_json(tb_request) from tb_request WHERE request_id=(%s)"""
        
        conn = None
        results = None
        try:
            conn=psycopg2.connect(DATABASE_URL())
            cur = conn.cursor()

            cur.execute(query,(request_id,))
            results = cur.fetchall()

            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            return error
        finally:
            if conn is not None:
                conn.close()
        
        return results


    def create_request(self, requestor,request_type,status,description,created_on):
        """create a request"""
        sql = """INSERT into tb_request (requestor,request_type,status,description,created_on)
                VALUES(%s,%s,%s,%s,%s)"""
        conn = None

        try:
            conn = psycopg2.connect(DATABASE_URL())
            cur = conn.cursor()

            cur.execute(sql, (requestor,request_type,status,description,created_on,))

            conn.commit()
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            return error
        finally:
            if conn is not None:
                conn.close()
        return "Data saved succesfully"
    
    def modify_request(request_type,description,last_modified,request_id):
        """Edit or modify a request"""
        query = """UPDATE tb_request SET request_type=%s,description=%s,
                    last_modified=%s WHERE request_id=%s;"""
    
        conn = None
        user_id = None
        try:
            #params = dbconfig(filename, section)
            conn = psycopg2.connect(DATABASE_URL())

            cur = conn.cursor()
            cur.execute(query,(request_type,description,last_modified,request_id,))

                
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            return error
        finally:
            if conn is not None:
                conn.close()
        return user_id
    
    def request_action(self, status, last_modified, request_id):
        #PUT /request/<id>/approve
        sql = """UPDATE tb_request SET status=%s, last_modified=%s WHERE request_id=%s"""

        conn = None
        try:
            conn = psycopg2.connect(DATABASE_URL())
            cur = conn.cursor()
            cur.execute(sql,(status,last_modified, request_id,))

                
            conn.commit()
            cur.close()


        except (Exception, psycopg2.DatabaseError) as error:
            return error
        
        finally:
            if conn is not None:
                conn.close()
    