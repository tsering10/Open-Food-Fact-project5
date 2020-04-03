
from connect_mysql import connect
from sqlalchemy import inspect

import pandas as pd

# filename = '/home/tashitsering/Openfood project/open_food_data/open_food_data.csv'
# df = pd.read_csv(filename)
# print(df.head())
# print('-------------------------------------------------------------------')
# print(df['main_category'].unique())

def model():
    cursor = connect()
    print(cursor)
    #cursor.execute("SHOW DATABASES;")
    #databases = cursor.fetchall() ## it returns a list of all databases present

#     ## printing the list of databases
    #print(databases)

 
# def test_connection(conn):
#     cursor = conn.cursor()
#    # cursor.execute("CREATE DATABASE datacamp")

#     #cursor.execute("DROP SCHEMA IF EXISTS datacamp;")
#     #cursor.execute("CREATE SCHEMA IF NOT EXISTS datacamp DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;")

#     cursor.execute("SHOW DATABASES;")
#     databases = cursor.fetchall() ## it returns a list of all databases present

#     ## printing the list of databases
#     print(databases)

#     filename = '/home/tashitsering/Openfood project/open_food_data/open_food_data.csv'
#     df = pd.read_csv(filename)
#     print(df.head())
#     cat = df[pd.notnull(df['main_category'])]['main_category'].unique().tolist()
#     print(cat)


#     DB_NAME = 'datacamp'
#     cursor.execute("USE {}".format(DB_NAME))
#     TABLES = {}

#     TABLES['category'] = (
#     "CREATE TABLE `category` ("
#     "`id` INT UNSIGNED NOT NULL AUTO_INCREMENT,"
#     " `category_name` varchar(14) NOT NULL,"
#     "  PRIMARY KEY (`id`)"
#     ") ENGINE=InnoDB")
#     for table_name in TABLES:
#         table_description = TABLES[table_name]
#         try:
#             print("Creating table {}: ".format(table_name), end='')
#             cursor.execute(table_description)
#         except mysql.connector.Error as err:
#             if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#                 print("already exists.")
#             else:
#                 print(err.msg)
#         else:
#             print("OK")
    
#     add_cat = ("INSERT INTO category"
#                "(category_name) "
#                "VALUES (%s)")
#     cursor.execute(add_cat,'cereal')

    # for i in cat:
    #     add_cat = ("INSERT INTO category VALUES (%(category_name)s)")
    #     cursor.execute(add_cat,i)

# def test_connection(mysql_engine):
#     print(mysql_engine.url)

    



if __name__ == "__main__":
    model()
    