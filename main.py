"""the program starts from this file"""

from core.user import User
from data import menus, prompts
from services.car_services.vendor_manage_car import manage_cars
from services.user_services.authenticate_user import authenticate_user
from services.user_services.get_user_id_by_email import get_user_id_by_email
from services.user_services.load_user_data_from_db import load_user_data
from utils.get_user_option import get_user_option
from utils.input_handler import UserInputHandler


def display_main_menu():
    """the main menu for the app"""
    while True:
        print(prompts.WELCOME)
        opt = get_user_option(menus.welcome_menu, prompts.STANDARD_MENU)
        if opt == 0:
            break
        if opt == 1:
            login_user()
        if opt == 2:
            register_user()


def login_user():
    """authenticates and login the user"""
    email = UserInputHandler.get_valid_email("Enter your account Email to Login: ")
    password = input("Enter your Account Password: ")
    if authenticate_user(email, password):
        user_id = get_user_id_by_email(email)
        user = load_user_data(user_id)
        if user:
            handle_login_menu(user)
        else:
            print(prompts.DATA_LOADING_FAILED)
    else:
        print(prompts.LOGIN_FAILED)


def register_user():
    """creates a new user object"""
    print("\nEnter your details to register. Press 'CTRL+C' to Exit anytime.\n")
    username = UserInputHandler.get_valid_username("Enter Your Username: ")
    user_role = UserInputHandler.get_valid_user_role(
        "Select Your User Role (Customer/Vendor): "
    )
    first_name = UserInputHandler.get_valid_first_name("Enter Your First Name: ")
    last_name = UserInputHandler.get_valid_last_name("Enter Your Last Name: ")
    gender = UserInputHandler.get_valid_gender("Select Your Gender (M/F/O): ")
    date_of_birth = UserInputHandler.get_valid_date_of_birth(
        "Enter Your Date of Birth(YY-MM-DD): "
    )
    email = UserInputHandler.get_valid_email("Enter Your Email: ")
    user_password = UserInputHandler.get_valid_password("Enter Your Password: ")
    phone_number = UserInputHandler.get_valid_phone_no("Enter Your Phone Number: ")
    user = User(
        username,
        user_role,
        first_name,
        last_name,
        gender,
        date_of_birth,
        email,
        user_password,
        phone_number,
    )
    print(prompts.REGISTER_SUCCESS)
    handle_login_menu(user)


def handle_login_menu(user):
    """displays the login menu based on user"""
    print(
        prompts.WELCOME_LOGIN_TEXT.format(
            prompts.DASHES, user.first_name, user.last_name, prompts.DASHES
        )
    )
    if user.user_role == "Customer":
        customer_menu(user)
    elif user.user_role == "Vendor":
        vendor_menu(user)
    elif user.user_role == "Admin":
        admin_menu(user)


def customer_menu(customer):
    """customer menu handling"""
    while True:
        opt = get_user_option(menus.customer_login_menu, prompts.STANDARD_MENU)
        if opt == 0:
            break
        if opt == 1:
            pass
        if opt == 2:
            pass


def vendor_menu(vendor):
    """vendor menu handling"""
    while True:
        opt = get_user_option(menus.vendor_login_menu, prompts.STANDARD_MENU)
        if opt == 0:
            break
        if opt == 1:
            manage_cars(vendor)
        if opt == 2:
            pass


def admin_menu(admin):
    """admin menu handling"""
    while True:
        opt = get_user_option(menus.admin_login_menu, prompts.STANDARD_MENU)
        if opt == 0:
            break
        if opt == 1:
            pass
        if opt == 2:
            pass


def main():
    """loads the program and calls the menu"""
    display_main_menu()
    print(prompts.EXIT)


main()
