"""fetched user data using given user id"""

from mysql.connector import Error
from config.db_connection import create_connection
from data import prompts, users_queries


def get_data_by_user_id(user_id):
    """fetched user data using given user id"""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(users_queries.GET_USER_DATA_BY_ID, (user_id,))
        user = cursor.fetchone()
        if user:
            return user
        return False
    except Error as e:
        print(prompts.DB_ERROR.format(e))
        return False
    finally:
        cursor.close()
        conn.close()
