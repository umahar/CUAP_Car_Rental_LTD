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


def get_all_notifications(user_id, sort_by="DESC"):
    """fetches all unread notifications"""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        query = f"""SELECT * FROM notifications WHERE user_id = %s ORDER BY created_at {sort_by};"""
        cursor.execute(query, (int(user_id),))
        rows = cursor.fetchall()
        return rows
    except Error as e:
        print(prompts.DB_ERROR.format(e))
        return None
    finally:
        cursor.close()
        conn.close()


def get_all_unread_notifications(user_id, sort_by="DESC"):
    """fetches all unread notifications"""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        query = f"""SELECT * FROM notifications WHERE user_id = %s and is_read = 0 ORDER BY created_at {sort_by};"""
        cursor.execute(query, (int(user_id),))
        rows = cursor.fetchall()
        return rows
    except Error as e:
        print(prompts.DB_ERROR.format(e))
        return None
    finally:
        cursor.close()
        conn.close()


def get_notifications_by_category(user_id, category, sort_by="DESC"):
    """fetches all notifications based on a category"""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        query = f"""SELECT * FROM notifications WHERE user_id = %s and category={category} ORDER BY created_at {sort_by};"""
        cursor.execute(query, (int(user_id),))
        rows = cursor.fetchall()
        return rows
    except Error as e:
        print(prompts.DB_ERROR.format(e))
        return None
    finally:
        cursor.close()
        conn.close()


def delete_notifications(user_id):
    """deletes notifications of a user_id"""

    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(notifications_queries.DELETE_ALL_NOTIFICATIONS, (user_id,))
        conn.commit()
        return True
    except Error as e:
        print(prompts.DB_ERROR.format(e))
        return False
    finally:
        cursor.close()
        conn.close()


def mark_notification_read(notifications):
    """marks each notification as read"""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        for notification in notifications:
            notification_id = notification[0]
            if notification[3] == 0:
                cursor.execute(
                    notifications_queries.MARK_AS_READ,
                    (int(notification_id),),
                )
        conn.commit()
        return True
    except Error as e:
        print(prompts.DB_ERROR.format(e))
        return None
    finally:
        cursor.close()
        conn.close()
