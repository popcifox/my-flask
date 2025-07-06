# db.py
import pymysql
from pymysql.cursors import DictCursor
db_config = {
    'host': '127.0.0.1',
    'port' : 3306,
    'user': 'root',
    'password': '1234',
    'database': 'my_db',
    'charset': 'utf8mb4',
    'cursorclass': DictCursor
}

def get_connection():
    return pymysql.connect(**db_config)
