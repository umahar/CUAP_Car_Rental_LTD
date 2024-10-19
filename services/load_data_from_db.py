"""loads all the saved data from the DB"""

from core.user import User
from services.get_all_users import get_all_users


def load_data():
    """gets all data from DB"""
    users = get_all_users()
    if users:
        for user in users:
            old_user = User(
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
        return True
    return False
