"""all queries of notifications table"""

ADD_NOTIFICATION = """
INSERT INTO notifications(
    user_id,notification_message,category
    ) 
VALUES (%s, %s,%s);
"""

GET_ALL_NOTIFICATIONS = """SELECT * FROM notifications WHERE user_id = %s;"""

GET_ALL_NOTIFICATIONS_CW = (
    """SELECT * FROM notifications WHERE user_id = %s and category = %s;"""
)

GET_UNREAD_NOTIFICATIONS = (
    """SELECT * FROM notifications WHERE user_id = %s and is_read = 0;"""
)

GET_UNREAD_NOTIFICATIONS_CW = """
SELECT * FROM notifications WHERE user_id = %s and is_read = 0 and category = %s;"""

GET_READ_NOTIFICATIONS = (
    """SELECT * FROM notifications WHERE user_id = %s and is_read = 1;"""
)

GET_READ_NOTIFICATIONS_CW = """
SELECT * FROM notifications WHERE user_id = %s and is_read = 1 and category = %s;
"""
