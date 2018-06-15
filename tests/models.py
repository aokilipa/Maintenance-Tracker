#models tests

import flask
import datetime
import psycopg2

from passlib.hash import pbkdf2_sha256 as sha256
from run import create_app
from flask_bcrypt import Bcrypt




def create_tables():
    """create tables in postgresql database"""
    commands = (
        """
        DROP TABLE IF EXISTS tb_users;
        CREATE TABLE tb_users(
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(100) UNIQUE NOT NULL,
            firstname VARCHAR(50) NOT NULL,
            lastname VARCHAR(50) NOT NULL,
            password VARCHAR(255) NOT NULL,
            created_on TIMESTAMP NOT NULL,
            last_login TIMESTAMP
        )
        """
        ,
        """
        DROP TABLE IF EXISTS tb_request;
        CREATE TABLE tb_request(
            request_id SERIAL PRIMARY KEY,
            requestor VARCHAR(255) NOT NULL,
            email VARCHAR(100) NOT NULL,
            type VARCHAR(50) NOT NULL,
            status VARCHAR(50) NOT NULL,
            description TEXT,
            created_on TIMESTAMP NOT NULL
        )
        """
        ,
        """
        DROP TABLE IF EXISTS tb_admin;
        CREATE TABLE tb_admin(
            admin_id SERIAL PRIMARY KEY,
            username VARCHAR(100) UNIQUE NOT NULL,
            fullname VARCHAR(100) NOT NULL,
            password VARCHAR(255) NOT NULL,
            created_on TIMESTAMP NOT NULL,
            last_login TIMESTAMP
        )
        """
    )

    conn = None
    try:
        
        conn = psycopg2.connect(dbname='test_db',user="antonio", password="pass.123")

        #create cursor
        cur = conn.cursor()
        
        #execute statement
        for command in commands:
            cur.execute(command)

        cur.close()

        #commit the changes
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    
    return "Tables user, request and admin created succesfully"


def insert_to_db(self, username, password, firstname, lastname, created_on):
    """insert a new user into database"""

    query = """INSERT INTO tb_users (username, password, firstname, lastname, created_on)
                VALUES(%s,%s,%s,%s,%s)"""
    
    conn = None
    user_id = None
    try:
        
        conn = psycopg2.connect(dbname='test_db',user="antonio", password="pass.123")

        cur = conn.cursor()
        cur.execute(query,(username, password, firstname, 
                    lastname, created_on,))

               
        conn.commit()
        user_id = cur.fetchone()[0]
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return user_id

def find_by_username(username):
    query = """SELECT username,password FROM tb_users WHERE username=(%s)"""
    
    conn = None
    result = None
    try:
        conn = psycopg2.connect(dbname='test_db',user="antonio", password="pass.123")

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
        conn = psycopg2.connect(dbname='test_db',user="antonio", password="pass.123")

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