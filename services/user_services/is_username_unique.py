"""checks to see if a provided username is unique"""

from mysql.connector import Error
from config.db_connection import create_connection
from data import prompts, users_queries


def is_username_unique(given_username):
    """checks to see if a provided username is unique"""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(users_queries.GET_USER_BY_USERNAME, (given_username,))
        user = cursor.fetchone()
        if user:
            return False
        return True
    except Error as e:
        print(prompts.DB_ERROR.format(e))
        return False
    finally:
        cursor.close()
        conn.close()
