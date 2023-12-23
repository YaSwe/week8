import json
import mysql.connector
from mysql.connector import Error

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

def get_database_connection():
    with open('config.json') as config_file:
        config = json.load(config_file)

    db_host = config['DB_HOST']
    db_user = config['DB_USER']
    db_password = config['DB_PASSWORD']
    db_name = config['DB_DATABASE']

    return create_server_connection(db_host, db_user, db_password, db_name)
