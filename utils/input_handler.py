"""this file will call the relevant input validation function and return prompts"""

from utils.input_check import CheckInput
from data import prompts


class UserInputHandler:
    """this file will call the relevant input validation function and return prompts"""

    @staticmethod
    def get_valid_username(prompt):
        """This function will prompt the user to keep entering username
        and validating it until it's correct."""
        username = input(prompt)
        while not CheckInput.is_valid_username(username):
            print(prompts.INVALID_INPUT)
            username = input(prompt)
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
    def get_valid_email(prompt):
        """this function will prompt the user to keep entering email
        and validating it until its correct"""
        email = input(prompt)
        while not CheckInput.is_valid_email(email):
            print(prompts.INVALID_INPUT)
            email = input(prompt)
        return email

    @staticmethod
    def get_valid_password(prompt):
        """this function will prompt the user to keep entering password
        and validating it until its correct"""
        password = input(prompt)
        while not CheckInput.is_valid_password(password):
            print(prompts.INVALID_INPUT)
            password = input(prompt)
        return password

    @staticmethod
    def get_valid_phone_no(prompt):
        """this function will prompt the user to keep entering phone no
        and validating it until its correct"""
        phone_no = input(prompt)
        while not CheckInput.is_valid_phone_no(phone_no):
            print(prompts.INVALID_INPUT)
            phone_no = input(prompt)
        return phone_no
