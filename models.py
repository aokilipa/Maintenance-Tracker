import psycopg2
from datetime import datetime
from config import dbconfig, basedir, filename , section, DATABASE_URL
import os
import jwt

from flask import json, jsonify
from itsdangerous import (TimedJSONWebSignatureSerializer 
                            as Serializer, BadSignature, SignatureExpired)





def connect():
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



if __name__ == '__main__':
    connect()

    
    