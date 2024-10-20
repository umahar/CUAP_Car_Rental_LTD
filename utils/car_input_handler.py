class CarInputHandler:
    """Handles the input validation and prompts for car details."""

    @staticmethod
    def get_valid_car_id(prompt):
        car_id = input(prompt)
        while not car_id.isdigit():
            print("Invalid car ID. Please enter a numeric value.")
            car_id = input(prompt)
        return int(car_id)

    @staticmethod
    def get_valid_vendor_id(prompt):
        vendor_id = input(prompt)
        while not vendor_id.isdigit():
            print("Invalid vendor ID. Please enter a numeric value.")
            vendor_id = input(prompt)
        return int(vendor_id)

    @staticmethod
    def get_valid_make(prompt):
        make = input(prompt)
        while len(make) == 0:
            print("Make cannot be empty.")
            make = input(prompt)
        return make

    @staticmethod
    def get_valid_model(prompt):
        model = input(prompt)
        while len(model) == 0:
            print("Model cannot be empty.")
            model = input(prompt)
        return model

    @staticmethod
    def get_valid_car_year(prompt):
        car_year = input(prompt)
        while not car_year.isdigit() or not (1900 <= int(car_year) <= 2100):
            print("Invalid year. Please enter a valid car year between 1900 and 2100.")
            car_year = input(prompt)
        return int(car_year)

    @staticmethod
    def get_valid_color(prompt):
        color = input(prompt)
        while len(color) == 0:
            print("Color cannot be empty.")
            color = input(prompt)
        return color

    @staticmethod
    def get_valid_car_type(prompt):
        car_types = ['SUV', 'Sedan', 'Hatchback', 'Truck', 'Van', 'Coupe', 'Convertible', 'Wagon', 'Other']
        car_type = input(prompt)
        while car_type not in car_types:
            print(f"Invalid car type. Please choose from {car_types}.")
            car_type = input(prompt)
        return car_type

    @staticmethod
    def get_valid_rental_price_per_day(prompt):
        rental_price = input(prompt)
        while not rental_price.replace('.', '', 1).isdigit():
            print("Invalid rental price. Please enter a numeric value.")
            rental_price = input(prompt)
        return float(rental_price)

    @staticmethod
    def get_valid_mileage(prompt):
        mileage = input(prompt)
        while not mileage.isdigit():
            print("Invalid mileage. Please enter a numeric value.")
            mileage = input(prompt)
        return int(mileage)

    @staticmethod
    def get_valid_car_location(prompt):
        location = input(prompt)
        while len(location) == 0:
            print("Car location cannot be empty.")
            location = input(prompt)
        return location

    @staticmethod
    def get_valid_is_available(prompt):
        is_available = input(prompt).lower()
        while is_available not in ['true', 'false']:
            print("Invalid input. Please enter 'true' or 'false'.")
            is_available = input(prompt).lower()
        return is_available == 'true'
