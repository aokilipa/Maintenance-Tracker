from flask import Flask
import datetime
import psycopg2

from passlib.hash import pbkdf2_sha256 as sha256
from run import create_app
from config import dbconfig, filename ,section, app_config, DATABASE_URL
from flask_bcrypt import Bcrypt

app = Flask(__name__)

def insert_to_db(self, username, password, firstname, lastname, created_on):
    """insert a new user into database"""

    query = """INSERT INTO tb_users (username, password, firstname, lastname, created_on)
                VALUES(%s,%s,%s,%s,%s)"""
    
    conn = None
    user_id = None
    try:
        #params = dbconfig(filename, section)
        conn = psycopg2.connect(DATABASE_URL())

        cur = conn.cursor()
        cur.execute(query,(username, password, firstname, 
                    lastname, created_on,))

               
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
    query = """SELECT username,password FROM tb_users WHERE username=(%s)"""
    
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
        print (error)
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

class RevokedTokenModel(object):
    pass