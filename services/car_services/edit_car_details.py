"""edits a given car detail"""

from mysql.connector import Error
from data import prompts
from config.db_connection import create_connection
from services.car_services.delete_car import delete_car_by_id
from services.notification_services.notification import add_new_notification
from services.user_services.get_vendor_by_car import get_vendor_by_car_id


def edit_car_detail(car_id, item_to_edit, current_value, new_value=""):
    """edits allowed detail"""
    if edit_car_item(car_id, item_to_edit, new_value):
        print(f"\nChanging detail '{current_value}' to '{new_value}'.")
        print(prompts.UPDATE_SUCCESSFUL)
        add_new_notification(
            user_id=get_vendor_by_car_id(car_id),
            notification_message="CAR UPDATED",
            category="Cars",
        )


def manage_delete(car_id):
    """handles delete car"""
    vendor_id = get_vendor_by_car_id(car_id)
    print("\nType 'DELETE' to remove the car. THIS CAN NOT BE UNDONE.\n")
    res = input("RESPONSE: ")
    if res == "DELETE":
        if delete_car_by_id(car_id):
            print(prompts.CAR_DELETED)
            add_new_notification(
                user_id=vendor_id,
                notification_message="CAR DELETED",
                category="Cars",
            )
        else:
            print(prompts.UNKNOWN_ERROR)
    else:
        print(prompts.INVALID_INPUT)


def edit_car_item(car_id, item_to_edit, new_value):
    """edits car detail in DB"""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        update_car_sql = f"UPDATE cars SET {item_to_edit} = %s WHERE car_id=%s;"
        cursor.execute(update_car_sql, (new_value, car_id))
        conn.commit()
        return True
    except Error as e:
        print(prompts.DB_ERROR.format(e))
        return None
    finally:
        cursor.close()
        conn.close()
