"""fetches car data using given car id"""

from mysql.connector import Error
from config.db_connection import create_connection
from data import prompts, cars_queries


def get_data_by_car_id(car_id):
    """fetched car data using given car id"""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(cars_queries.GET_CAR_DATA_BY_ID, (car_id,))
        car = cursor.fetchone()
        if car:
            return car
        return False
    except Error as e:
        print(prompts.DB_ERROR.format(e))
        return False
    finally:
        cursor.close()
        conn.close()
