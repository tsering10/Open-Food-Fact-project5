
from mysql.connector import Error
from sqlalchemy import create_engine
import sqlalchemy
from python_mysql_dbconfig import read_db_config


def connect():
    """ function to Connect a MySQL database """
    db_config = read_db_config()
    try:
        # mysql connection link url  
        mysql_connection_url = f"mysql+mysqlconnector://root:{db_config['password']}@{db_config['host']}:3306/"
        mysql_engine = sqlalchemy.create_engine(mysql_connection_url)
        # Query for checking existing databases
        mysql_engine.execute(f"CREATE DATABASE IF NOT EXISTS {db_config['database']}")
        # Go ahead and use this engine
        db_engine = create_engine(f"{mysql_connection_url}{db_config['database']}")
        if db_engine.connect():
            return db_engine
        else:
            print('Connection Failed')
    except Error as error:
        print(error)




 
