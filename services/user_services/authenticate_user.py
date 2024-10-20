"""authenticates a user based on email and password"""

from mysql.connector import Error
from config.db_connection import create_connection
from data import prompts, users_queries


def authenticate_user(email, user_password):
    """matches email and password"""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(users_queries.GET_USER_PASSWORD_BY_EMAIL, (email,))
        fetched_pass = cursor.fetchone()
        if fetched_pass:
            if fetched_pass[0] == user_password:
                return True
        return False
    except Error as e:
        print(prompts.DB_ERROR.format(e))
        return False
    finally:
        cursor.close()
        conn.close()
