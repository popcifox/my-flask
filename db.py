# db.py
import pymysql
from pymysql.cursors import DictCursor
db_config = {
    'host': '43.200.6.22',
    'port' : 3306,
    'user': 'user',
    'password': '1234',
    'database': 'my_db',
    'charset': 'utf8mb4',
    'cursorclass': DictCursor
}

def get_connection():
    return pymysql.connect(**db_config)
