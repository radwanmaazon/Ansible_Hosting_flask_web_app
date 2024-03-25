import mysql.connector

__mydb = None
def get_sql_connection():
    global __mydb

    if __mydb is None:

        __mydb = mysql.connector.connect(
            host="192.168.1.185",
            user="appuser",
            password="appuser",
            database="gs"
        )

        # __mydb = mysql.connector.connect(
        #     host="localhost",
        #     user="radwan",
        #     password="rDI@rdi123",
        #     database="gs"
        # )

    return __mydb
