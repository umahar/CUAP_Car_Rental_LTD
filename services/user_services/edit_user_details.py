"""edits a given user detail"""

import os
import sys
from mysql.connector import Error
from data import prompts
from services.notification_services.notification import add_new_notification
from services.user_services.delete_user import delete_user
from services.user_services.get_user_id_by_email import get_user_id_by_email
from config.db_connection import create_connection


def edit_user_detail(user, item_to_edit, new_value=""):
    """edits allowed detail"""
    if item_to_edit == "DELETE":
        manage_delete(user.username)
    else:
        current_value = getattr(user, item_to_edit)
        if edit_user_item(user.username, item_to_edit, new_value):
            setattr(user, item_to_edit, new_value)
            print(f"\nChanging detail '{current_value}' to '{new_value}'.")
            print(prompts.UPDATE_SUCCESSFUL)
            add_new_notification(
                user_id=get_user_id_by_email(user.email),
                notification_message="PROFILE UPDATED",
                category="Account/Profile",
            )


def manage_delete(username):
    """handles delete user"""
    print("\nType 'DELETE' to remove the profile. THIS CAN NOT BE UNDONE.\n")
    res = input("RESPONSE: ")
    if res == "DELETE":
        if delete_user(username):
            print(prompts.USER_DELETED)
            print(prompts.LOGOUT)
            python = sys.executable
            os.execv(python, [python] + sys.argv)
        else:
            print(prompts.UNKNOWN_ERROR)
    else:
        print(prompts.INVALID_INPUT)


def edit_user_item(username, item_to_edit, new_value):
    """edits user detail in DB"""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        update_user_sql = f"UPDATE users SET {item_to_edit} = %s WHERE username=%s;"
        cursor.execute(update_user_sql, (new_value, username))
        conn.commit()
        return True
    except Error as e:
        print(prompts.DB_ERROR.format(e))
        return None
    finally:
        cursor.close()
        conn.close()
