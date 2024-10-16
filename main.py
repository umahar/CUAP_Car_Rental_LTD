"""the program starts from this file"""

from data import menus, prompts
from utils.get_user_option import get_user_option
from utils.input_handler import UserInputHandler


def display_main_menu():
    """the main menu for the app"""
    print(prompts.WELCOME)
    opt = get_user_option(menus.welcome_menu, prompts.STANDARD_MENU)
    if opt == 0:
        login_user()
    if opt == 1:
        register_user()


def login_user():
    """authenticates and login the user"""


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


def load_data():
    """loads the data from the db"""


def main():
    """loads the program and calls the menu"""
    # load data from db
    display_main_menu()


main()
