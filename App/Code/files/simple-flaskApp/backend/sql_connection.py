import configparser
import mysql.connector

__mydb = None
def get_sql_connection():
    global __mydb

    if __mydb is None:

        __mydb = mysql.connector.connect(
            host="192.168.1.74",
            port="6033",
            user="playgrounduser",
            password="{{ playgrounduser_pass }}",
            database="gs"
        )
        
    return __mydb
