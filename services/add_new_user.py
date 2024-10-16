"""adds a new user to users table in DB"""

from mysql.connector import Error
from config.db_connection import create_connection


def add_new_user(user):
    """adds user to DB"""
    conn = create_connection()
