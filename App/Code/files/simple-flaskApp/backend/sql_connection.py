import mysql.connector

__mydb = None
def get_sql_connection():
    global __mydb

    if __mydb is None:

        __mydb = mysql.connector.connect(
            host="db1.mydomain.org",
            user="appuser",
            password="appuser" ,
            database="gs"
        )
        
    return __mydb
