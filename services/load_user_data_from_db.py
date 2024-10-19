"""loads all the saved data from the DB"""

from core.user import User
from services.get_data_by_user_id import get_data_by_user_id


def load_user_data(user_id):
    """gets all data of a user from DB"""
    user = get_data_by_user_id(user_id)
    if user:
        new_user = User(
            username=user[1],
            user_role=user[2],
            first_name=user[3],
            last_name=user[4],
            gender=user[5],
            date_of_birth=user[6].strftime("%Y-%m-%d"),
            email=user[7],
            user_password=user[8],
            phone_number=user[9],
            is_new_user=False,
        )
        return new_user
    return False
