"""adds a new user to users table in DB"""

from mysql.connector import Error
from config.db_connection import create_connection
from data import prompts, users_queries


def add_new_user(user):
    """adds user to DB"""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            users_queries.ADD_USER,
            (
                user.username,
                user.user_role,
                user.first_name,
                user.last_name,
                user.gender,
                user.date_of_birth,
                user.email,
                user.user_password,
                user.phone_number,
            ),
        )
        conn.commit()
        return True
    except Error as e:
        print(prompts.DB_ERROR.format(e))
        return None
    finally:
        cursor.close()
        conn.close()
