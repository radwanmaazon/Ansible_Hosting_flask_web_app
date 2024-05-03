import configparser
import mysql.connector

__mydb = None

def get_sql_connection():
    global __mydb

    if __mydb is None:
        config = configparser.ConfigParser()
        config.read('config.ini')

        db_config = {
            'host': config['database']['host'],
            'port': config['database']['port'],
            'user': config['database']['user'],
            'password': config['database']['password'],
            'database': config['database']['name']
        }

        __mydb = mysql.connector.connect(**db_config)

    return __mydb
