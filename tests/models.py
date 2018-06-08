import os
import psycopg2
from models import connect


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
        

if __name__ == '__main__':
    create_tables()