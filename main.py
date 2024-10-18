"""the program starts from this file"""

from core.user import User
from data import menus, prompts
from services.authenticate_user import authenticate_user
from services.get_data_by_user_id import get_data_by_user_id
from services.get_user_id_by_email import get_user_id_by_email
from services.load_data_from_db import load_data
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
            register_user()
        if opt == 2:
            login_user()


def login_user():
    """authenticates and login the user"""
    email = UserInputHandler.get_valid_email("Enter your account Email to Login: ")
    password = input("Enter your Account Password: ")
    if authenticate_user(email, password):
        user_id = get_user_id_by_email(email)
        display_login_menu(user_id)
    else:
        print(prompts.LOGIN_FAILED)


def register_user():
    """creates a new user object"""
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
    user_id = get_user_id_by_email(email)
    display_login_menu(user_id)


def display_login_menu(user_id):
    """displays the login menu based on user"""
    user_data = get_data_by_user_id(user_id)
    print(
        prompts.WELCOME_LOGIN_TEXT.format(
            prompts.DASHES, user_data[3], user_data[4], prompts.DASHES
        )
    )


def main():
    """loads the program and calls the menu"""
    if load_data():
        display_main_menu()
        print(prompts.EXIT)
    else:
        print(prompts.DATA_LOADING_FAILED)


main()
