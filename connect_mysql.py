# from mysql.connector import MySQLConnection, Error
# from python_mysql_dbconfig import read_db_config
 
 
# def connect():
#     """ Connect to MySQL database """
#     db_config = read_db_config()
#     conn = None
#     try:
#         print('Connecting to MySQL database...')
#         conn = MySQLConnection(**db_config)

 
#         if conn.is_connected():
#             print('Connection established.')

#             return conn

           
#         else:
#             print('Connection failed.')
 
#     except Error as error:
#         print(error)
 
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from sqlalchemy_utils import database_exists


def connect():
    """ Connect to MySQL database """
    db_config = read_db_config()
    dbName = 'test'
    #conn = None
    
    
    try:
        print('Connecting to MySQL database...')
        mysql_connection_url = f"mysql+mysqlconnector://root:{db_config['password']}@{db_config['host']}:3306/"
       
        mysql_engine = sqlalchemy.create_engine(mysql_connection_url)

        # Query for existing databases
        mysql_engine.execute(f"CREATE DATABASE IF NOT EXISTS {dbName}")

        # Go ahead and use this engine
        db_engine = create_engine(f"mysql+mysqlconnector://root:{db_config['password']}@{db_config['host']}:3306/{dbName}")

        if db_engine.connect():
            print('Connection established')
        else:
            print('Connection Failed')


    
 
    except Error as error:
        print(error)



connect()

 
