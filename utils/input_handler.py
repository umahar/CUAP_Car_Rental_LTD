"""this file will call the relevant input validation function and return prompts"""

from services.user_services.is_email_unique import is_email_unique
from services.user_services.is_username_unique import is_username_unique
from utils.input_check import CheckInput
from data import prompts


class UserInputHandler:
    """this file will call the relevant input validation function and return prompts"""

    @staticmethod
    def get_valid_username(prompt, unique_check=True):
        """This function will prompt the user to keep entering username
        and validating it until it's correct."""
        while True:
            username = input(prompt)
            if not CheckInput.is_valid_username(username):
                print(prompts.INVALID_INPUT)
                continue
            if unique_check:
                if not is_username_unique(username):
                    print(prompts.INVALID_USERNAME)
                    continue
            return username

    @staticmethod
    def get_valid_user_role(prompt):
        """This function will prompt the user to keep entering user role
        and validating it until it's correct."""
        role = input(prompt)
        while not CheckInput.is_valid_user_role(role):
            print(prompts.INVALID_INPUT)
            role = input(prompt)
        return role

    @staticmethod
    def get_valid_first_name(prompt):
        """this function will prompt the user to keep entering name
        and validating it until its correct"""
        name = input(prompt)
        while not CheckInput.is_valid_name(name):
            print(prompts.INVALID_INPUT)
            name = input(prompt)
        return name

    @staticmethod
    def get_valid_last_name(prompt):
        """this function will prompt the user to keep entering name
        and validating it until its correct"""
        name = input(prompt)
        while not CheckInput.is_valid_name(name):
            print(prompts.INVALID_INPUT)
            name = input(prompt)
        return name

    @staticmethod
    def get_valid_gender(prompt):
        """this function will prompt the user to keep entering gender
        and validating it until its correct"""
        gender = input(prompt)
        while gender not in ["M", "F", "O"]:
            print(prompts.INVALID_INPUT)
            gender = input(prompt)
        return gender

    @staticmethod
    def get_valid_date_of_birth(prompt):
        """this function will prompt the user to keep entering date of birth
        and validating it until its correct"""
        dob = input(prompt)
        while not CheckInput.is_valid_dob(dob):
            print(prompts.INVALID_INPUT)
            dob = input(prompt)
        return dob

    @staticmethod
    def get_valid_email(prompt, unique_check=True):
        """this function will prompt the user to keep entering email
        and validating it until its correct"""
        while True:
            email = input(prompt)
            if not CheckInput.is_valid_email(email):
                print(prompts.INVALID_INPUT)
                continue
            if unique_check:
                if not is_email_unique(email):
                    print(prompts.INVALID_EMAIL)
                    continue
            return email

    @staticmethod
    def get_valid_user_password(prompt):
        """this function will prompt the user to keep entering password
        and validating it until its correct"""
        password = input(prompt)
        while not CheckInput.is_valid_password(password):
            print(prompts.INVALID_INPUT)
            password = input(prompt)
        return password

    @staticmethod
    def get_valid_phone_number(prompt):
        """this function will prompt the user to keep entering phone no
        and validating it until its correct"""
        phone_no = input(prompt)
        while not CheckInput.is_valid_phone_no(phone_no):
            print(prompts.INVALID_INPUT)
            phone_no = input(prompt)
        return phone_no
