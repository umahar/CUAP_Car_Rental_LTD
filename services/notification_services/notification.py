"""manages notifications table in DB"""

from mysql.connector import Error
from config.db_connection import create_connection
from data import prompts, notifications_queries


def add_new_notification(user_id, notification_message, category):
    """adds notification to DB"""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            notifications_queries.ADD_NOTIFICATION,
            (int(user_id), notification_message, category),
        )
        conn.commit()
        return True
    except Error as e:
        print(prompts.DB_ERROR.format(e))
        return None
    finally:
        cursor.close()
        conn.close()
