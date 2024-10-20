"""car class boilerplate"""


class Car:
    """car class"""

    def __init__(
        self,
        vendor_id,
        make,
        model,
        car_year,
        color,
        car_type,
        rental_price_per_day,
        mileage,
        car_location,
        is_available=True,
    ):
        self.vendor_id = vendor_id
        self.make = make
        self.model = model
        self.car_year = car_year
        self.color = color
        self.car_type = car_type
        self.rental_price_per_day = rental_price_per_day
        self.mileage = mileage
        self.car_location = car_location
        self.is_available = is_available
