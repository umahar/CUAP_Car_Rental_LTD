"""deletes a car based on car_id"""

from mysql.connector import Error
from config.db_connection import create_connection
from data import prompts, users_queries


def delete_car_by_id(car_id):
    """deletes a car based on car id"""

    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(users_queries.DELETE_USER, (car_id,))
        conn.commit()
        return True
    except Error as e:
        print(prompts.DB_ERROR.format(e))
        return False
    finally:
        cursor.close()
        conn.close()
