"""checks to see if a provided email is unique"""

from mysql.connector import Error
from config.db_connection import create_connection
from data import prompts, users_queries


def is_email_unique(given_email):
    """checks to see if a provided email is unique"""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(users_queries.GET_USER_BY_EMAIL, (given_email,))
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
