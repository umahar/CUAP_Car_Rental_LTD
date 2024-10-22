"""fetches all cars from db"""

from mysql.connector import Error
from config.db_connection import create_connection
from data import prompts, cars_queries


def get_all_cars(vendor_id):
    """gets all cars stored"""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(cars_queries.GET_ALL_CARS, (vendor_id,))
        rows = cursor.fetchall()
        return rows
    except Error as e:
        print(prompts.DB_ERROR.format(e))
        return False
    finally:
        cursor.close()
        conn.close()
