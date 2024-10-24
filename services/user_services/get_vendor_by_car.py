"""fetches vendor id using given user email"""

from mysql.connector import Error
from config.db_connection import create_connection
from data import prompts, users_queries


def get_vendor_by_car_id(car_id):
    """fetched vendor_id using given user car_id"""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(users_queries.GET_VENDOR_ID_BY_CAR_ID, (car_id,))
        vendor_id = cursor.fetchone()
        if vendor_id:
            return vendor_id[0]
        return False
    except Error as e:
        print(prompts.DB_ERROR.format(e))
        return False
    finally:
        cursor.close()
        conn.close()
