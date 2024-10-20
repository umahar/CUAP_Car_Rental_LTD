"""fetches all users from db"""

from mysql.connector import Error
from config.db_connection import create_connection
from data import prompts, users_queries


def get_all_users():
    """gets all users stored"""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(users_queries.GET_ALL_USERS)
        rows = cursor.fetchall()
        return rows
    except Error as e:
        print(prompts.DB_ERROR.format(e))
        return False
    finally:
        cursor.close()
        conn.close()
