# config.py

import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Buithanhtai9#',  # Thay đổi thông tin kết nối cho đúng
        database='eventmanage'
    )
