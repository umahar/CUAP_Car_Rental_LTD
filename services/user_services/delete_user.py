"""deletes a user based on username"""

from mysql.connector import Error
from config.db_connection import create_connection
from data import prompts, users_queries


def delete_user(username):
    """deletes a user based on username"""

    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(users_queries.DELETE_USER, (username,))
        conn.commit()
        return True
    except Error as e:
        print(prompts.DB_ERROR.format(e))
        return False
    finally:
        cursor.close()
        conn.close()
