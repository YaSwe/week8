import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect (
            host = host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    
    return connection

load_dotenv()

def get_database_connection():
    db_host = os.getenv('DB_HOST')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_name = os.getenv('DB_DATABASE')

    return create_server_connection(db_host, db_user, db_password, db_name)

