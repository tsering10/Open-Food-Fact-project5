
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import sqlalchemy
from sqlalchemy import create_engine



def connect():
    """ Connect to MySQL database """
    db_config = read_db_config()
    dbName = 'tashi'
    #conn = None
    
    
    try:
        #print('Connecting to MySQL database...')
        mysql_connection_url = f"mysql+mysqlconnector://root:{db_config['password']}@{db_config['host']}:3306/"
       
        mysql_engine = sqlalchemy.create_engine(mysql_connection_url)

        # Query for existing databases
        mysql_engine.execute(f"CREATE DATABASE IF NOT EXISTS {dbName}")

        # Go ahead and use this engine
        db_engine = create_engine(f"mysql+mysqlconnector://root:{db_config['password']}@{db_config['host']}:3306/{dbName}")
        


        if db_engine.connect():
            #print('Connection established')
            #conn = db_engine.connect()
            return db_engine
        else:
            print('Connection Failed')


    
 
    except Error as error:
        print(error)




 
