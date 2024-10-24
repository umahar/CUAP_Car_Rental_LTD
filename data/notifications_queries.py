"""all queries of notifications table"""

ADD_NOTIFICATION = """
INSERT INTO notifications(
    user_id,notification_message
    ) 
VALUES (%s, %s);
"""
