"""allows vendor to manage cars"""

from core.car import Car
from data import prompts
from services.car_services.add_new_car import add_new_car
from services.car_services.edit_car_details import edit_car_detail, manage_delete
from services.car_services.get_all_cars import get_all_cars
from services.car_services.get_data_by_car_id import get_data_by_car_id
from services.notification_services.notification import add_new_notification
from services.user_services.get_user_id_by_email import get_user_id_by_email
from utils.car_input_handler import CarInputHandler
from utils.get_user_option import get_user_option


def manage_cars(vendor):
    """allows vendor to manage cars"""
    vendor_id = get_user_id_by_email(vendor.email)
    while True:
        car_opt = get_user_option(
            ["Add a New Car", "View Cars", "Edit a Car", "Delete a Car"],
            prompts.STANDARD_MENU,
        )
        if car_opt == 0:
            break
        if car_opt == 1:
            register_car(vendor_id)
        if car_opt == 2:
            view_all_cars(vendor_id)
        if car_opt == 3:
            edit_car(vendor_id)
        if car_opt == 4:
            edit_car(vendor_id, delete=True)


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
    add_new_notification(
        user_id=vendor_id,
        notification_message="CAR REGISTERED",
        category="Cars",
    )


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


def manage_single_car(car_id):
    """handles car edits for all vendor"""
    car = get_data_by_car_id(car_id)
    print(prompts.MY_DETAILS)
    heading = "These are your current car details. Select any detail to edit below"
    car_menu = [
        f"Card ID: {car[0]}",
        f"MAKE: {car[2]}",
        f"MODEL: {car[3]}",
        f"YEAR: {car[4]}",
        f"COLOR: {car[5]}",
        f"TYPE: {car[6]}",
        f"PRICE/DAY: {car[7]}",
        f"MILEAGE: {car[8]}",
        f"LOCATION: {car[9]}",
    ]
    actions = {
        1: lambda: print(prompts.EDIT_NOT_ALLOWED),
        2: lambda: edit_car_detail(
            car_id,
            "make",
            car[2],
            new_value=CarInputHandler.get_valid_make("Enter Your new Car Make: "),
        ),
        3: lambda: edit_car_detail(
            car_id,
            "model",
            car[3],
            new_value=CarInputHandler.get_valid_model("Enter Your new Car Model: "),
        ),
        4: lambda: edit_car_detail(
            car_id,
            "car_year",
            car[4],
            new_value=CarInputHandler.get_valid_car_year("Enter Your new Car Year: "),
        ),
        5: lambda: edit_car_detail(
            car_id,
            "color",
            car[5],
            new_value=CarInputHandler.get_valid_color("Enter Your new Car Color: "),
        ),
        6: lambda: edit_car_detail(
            car_id,
            "car_type",
            car[6],
            new_value=CarInputHandler.get_valid_car_type("Enter Your new Car Type: "),
        ),
        7: lambda: edit_car_detail(
            car_id,
            "rental_price_per_day",
            car[7],
            new_value=CarInputHandler.get_valid_rental_price_per_day(
                "Enter Your new Car Price: "
            ),
        ),
        8: lambda: edit_car_detail(
            car_id,
            "mileage",
            car[8],
            new_value=CarInputHandler.get_valid_mileage("Enter Your new Car Mileage: "),
        ),
        9: lambda: edit_car_detail(
            car_id,
            "car_location",
            car[9],
            new_value=CarInputHandler.get_valid_car_location(
                "Enter Your new Car Location: "
            ),
        ),
    }

    opt = get_user_option(car_menu, heading)
    if opt in actions:
        actions[opt]()
    else:
        print(prompts.INVALID_INPUT)


def edit_car(vendor_id, delete=False):
    """edits a car of a vendor"""
    cars = get_all_cars(vendor_id)
    car_ids = []
    if cars:
        print(f"\nTOTAL CARS: {len(cars)}\n")
        for car in cars:
            car_ids.append(str(car[0]))
            print(
                f"\nCAR ID: {car[0]} || {car[2]} {car[3]} {car[4]} {car[5]} {car[6]} {car[7]} {car[8]} {car[9]}"
            )
        car_id = input("\nEnter the Car ID to manage: ")
        if car_id in car_ids:
            if delete:
                manage_delete(car_id)
            else:
                manage_single_car(car_id)
        else:
            print(prompts.INVALID_INPUT)
    else:
        print(prompts.NO_CARS)
