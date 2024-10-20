"""adds a new car to cars table in DB"""

from mysql.connector import Error
from config.db_connection import create_connection
from data import cars_queries, prompts


def add_new_car(car):
    """adds car to DB"""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            cars_queries.ADD_CAR,
            (
                car.vendor_id,
                car.make,
                car.model,
                car.car_year,
                car.color,
                car.car_type,
                car.rental_price_per_day,
                car.mileage,
                car.car_location,
            ),
        )
        conn.commit()
        return True
    except Error as e:
        print(prompts.DB_ERROR.format(e))
        return None
    finally:
        cursor.close()
        conn.close()
