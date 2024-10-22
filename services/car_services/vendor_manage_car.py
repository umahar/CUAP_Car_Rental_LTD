"""allows vendor to manage cars"""

from operator import index
from core.car import Car
from data import prompts
from services.car_services.add_new_car import add_new_car
from services.car_services.get_all_cars import get_all_cars
from services.user_services.get_user_id_by_email import get_user_id_by_email
from utils.car_input_handler import CarInputHandler
from utils.get_user_option import get_user_option


def manage_cars(vendor):
    """allows vendor to manage cars"""
    vendor_id = get_user_id_by_email(vendor.email)
    while True:
        car_opt = get_user_option(
            ["Add a New Car", "View Cars", "Delete a Car"], prompts.STANDARD_MENU
        )
        if car_opt == 0:
            break
        if car_opt == 1:
            register_car(vendor_id)
        if car_opt == 2:
            view_all_cars(vendor_id)
        if car_opt == 3:
            pass


def register_car(vendor_id):
    """Creates a new car object based on user input."""
    make = CarInputHandler.get_valid_make("Enter the Car Make: ")
    model = CarInputHandler.get_valid_model("Enter the Car Model: ")
    car_year = CarInputHandler.get_valid_car_year("Enter the Car Year: ")
    color = CarInputHandler.get_valid_color("Enter the Car Color: ")
    car_type = CarInputHandler.get_valid_car_type("Enter the Car Type: ")
    rental_price_per_day = CarInputHandler.get_valid_rental_price_per_day(
        "Enter the Rental Price per Day: "
    )
    mileage = CarInputHandler.get_valid_mileage("Enter the Mileage: ")
    car_location = CarInputHandler.get_valid_car_location("Enter the Car Location: ")
    car = Car(
        vendor_id,
        make,
        model,
        car_year,
        color,
        car_type,
        rental_price_per_day,
        mileage,
        car_location,
    )
    add_new_car(car)
    print(prompts.CAR_ADDED)


def view_all_cars(vendor_id):
    """shows all cars of the given vendor id"""
    cars = get_all_cars(vendor_id)
    if cars:
        print(f"\nTOTAL CARS: {len(cars)}\n")
        for car in cars:
            print(
                f"CAR ID: {car[0]}\n\nMAKE: {car[2]} | MODEL: {car[3]} | YEAR: {car[4]}\nCOLOR: {car[5]} | TYPE: {car[6]} | PRICE/DAY: {car[7]}\nMILEAGE: {car[8]} | LOCATION: {car[9]}\n\n"
            )

    else:
        print(prompts.NO_CARS)
