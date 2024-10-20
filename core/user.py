"""user class to handle customers,vendors & admin"""

from services.user_services.add_new_user import add_new_user


class User:
    """user class with 3 roles: Customer, Admin & Vendor"""

    def __init__(
        self,
        username,
        user_role,
        first_name,
        last_name,
        gender,
        date_of_birth,
        email,
        user_password,
        phone_number,
        is_new_user=True,
    ):
        self.username = username
        self.user_role = user_role
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.email = email
        self.user_password = user_password
        self.phone_number = phone_number
        if is_new_user:
            add_new_user(self)
