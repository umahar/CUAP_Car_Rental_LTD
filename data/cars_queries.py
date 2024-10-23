"""cars table queries"""

ADD_CAR = """
INSERT INTO cars(
    vendor_id,make,model,car_year,color,car_type,rental_price_per_day,mileage,car_location
    ) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
"""

GET_ALL_CARS = """SELECT * FROM cars WHERE vendor_id = %s;"""

DELETE_CAR = """DELETE FROM cars WHERE car_id = %s;"""

GET_CAR_DATA_BY_ID = """SELECT * from cars where car_id = %s;"""
