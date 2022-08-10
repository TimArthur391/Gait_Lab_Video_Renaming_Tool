from __future__ import print_function
import mysql.connector
import socket
from mysql.connector import errorcode

def connect_to_database(username, dAte, tIme, filename0, filename1, duration):
    try:
        ip = socket.gethostbyname(socket.gethostname())
        if ip == '192.168.32.225':
            cnx = mysql.connector.connect(user='root', 
                password='6395SQ134cz',
                host='localhost',
                port='3306',
                database='videorenamer',
                raise_on_warnings=True)
        else:
            cnx = mysql.connector.connect(user='Mar-system-user', 
                password='Thats-mar-bucket',
                host='10.211.147.242',
                port='3306',
                database='videorenamer',
                raise_on_warnings=True)
        cursor = cnx.cursor()

        add_usage = ("INSERT INTO usage_log (USERNAME, DATE, TIME, FILENAME0, FILENAME1, DURATION) VALUES (%s, %s, %s, %s, %s, %s)")
        data = (username, dAte, tIme, filename0, filename1, duration)

        cursor.execute(add_usage, data)

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
