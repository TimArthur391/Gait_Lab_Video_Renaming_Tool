from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode
import socket
import os
import dotenv

#Call get_request(SQL_statement, database_name) and post_request(SQL_statement, data, database_name)
#This calls the sub-function connect_to_db
#Database names = orlau_whr, version_control, videorenamer
#Examples of usage are give within each function


def connect_to_db(database_name):
    try:
        dotenv.load_dotenv()
        TEST_HOST_NAME=os.getenv("TEST_HOST_NAME")
        TEST_MYSQL_USER=os.getenv("TEST_MYSQL_USER")
        TEST_MYSQL_PASSWORD=os.getenv("TEST_MYSQL_PASSWORD")
        TEST_MYSQL_PORT=os.getenv("TEST_MYSQL_PORT")
        TEST_MYSQL_HOST=os.getenv("TEST_MYSQL_HOST")
        PROD_MYSQL_USER=os.getenv("PROD_MYSQL_USER")
        PROD_MYSQL_PASSWORD=os.getenv("PROD_MYSQL_PASSWORD")
        PROD_MYSQL_PORT=os.getenv("PROD_MYSQL_PORT")
        PROD_MYSQL_HOST=os.getenv("PROD_MYSQL_HOST")



        host=socket.gethostname()
        if host == TEST_HOST_NAME:
            cnx = mysql.connector.connect(user=TEST_MYSQL_USER, 
                password=TEST_MYSQL_PASSWORD,
                host=TEST_MYSQL_HOST,
                port=TEST_MYSQL_PORT,
                database=database_name,
                raise_on_warnings=True)
            print('Database connected successfully')
            return cnx
        else:
            cnx = mysql.connector.connect(user=PROD_MYSQL_USER, 
                password=PROD_MYSQL_PASSWORD,
                host=PROD_MYSQL_HOST,
                port=PROD_MYSQL_PORT,
                database=database_name,
                raise_on_warnings=True)
            print('Database connected successfully')
            return cnx
    
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

def get_request(SQL_statement, database_name):
    try:
        cnx = connect_to_db(database_name)
        cursor = cnx.cursor()

        #Example
        #SQL_statement = ("select MAX(RECORDID) as res from usage_log")
        cursor.execute(SQL_statement)

        query_results = cursor.fetchall() # or fetchone()

        cursor.close()
        cnx.close()

        return query_results


    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

def post_request(SQL_statement, data, database_name):
    try:
        cnx = connect_to_db(database_name)
        cursor = cnx.cursor()

        #Example
        #SQL_statement = ("INSERT INTO usage_log (USERNAME, DATE, TIME, FILENAME0, FILENAME1, DURATION) VALUES (%s, %s, %s, %s, %s, %s)")
        #data = (username, dAte, tIme, filename0, filename1, duration)
        cursor.execute(SQL_statement, data)

        cnx.commit()
        cursor.close()
        cnx.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)