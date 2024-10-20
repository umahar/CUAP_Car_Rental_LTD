"""cars table queries"""

ADD_CAR = """
INSERT INTO cars(
    vendor_id,make,model,car_year,color,car_type,rental_price_per_day,mileage,car_location
    ) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
"""
