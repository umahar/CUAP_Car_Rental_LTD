"""fetched user id using given user email"""

from mysql.connector import Error
from config.db_connection import create_connection
from data import prompts, users_queries


def get_user_id_by_email(email):
    """fetched user_id using given user email"""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(users_queries.GET_USER_ID_BY_EMAIL, (email,))
        user_id = cursor.fetchone()
        if user_id:
            return user_id[0]
        return False
    except Error as e:
        print(prompts.DB_ERROR.format(e))
        return False
    finally:
        cursor.close()
        conn.close()
