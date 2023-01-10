import mysql.connector
import sys


def connect_db():
    conn = None
    # create connection
    try:
        conn = mysql.connector.connect(host="localhost",
                                       port="3306",
                                       user="root",
                                       password="",
                                       database="taxi_app"
                                       )
    except:
        print("ERROR : ", sys.exc_info())

    finally:
        return conn
