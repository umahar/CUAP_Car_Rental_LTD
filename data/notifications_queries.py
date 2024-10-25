"""all queries of notifications table"""

ADD_NOTIFICATION = """
INSERT INTO notifications(
    user_id,notification_message,category
    ) 
VALUES (%s, %s,%s);
"""
DELETE_ALL_NOTIFICATIONS = """DELETE * FROM notifications WHERE user_id = %s;"""
