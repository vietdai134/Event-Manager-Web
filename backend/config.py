# config.py

import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345',  
        database='eventmanage'
    )
