"""handles profile edits for all user roles"""

from data import prompts
from services.user_services.edit_user_details import edit_user_detail
from utils.get_user_option import get_user_option


def manage_user_profile(user):
    """handles profile edits for all user roles"""
    heading = "This is your current profile. Select any detail to edit below"
    profile_menu = [
        f"Username: {user.username}",
        f"User Role: {user.user_role}",
        f"First Name: {user.first_name.capitalize()}",
        f"Last Name: {user.last_name.capitalize()}",
        f"Gender: {user.gender}",
        f"DOB: {user.date_of_birth}",
        f"Email: {user.email}",
        f"Password: {user.user_password}",
        f"Phone No: {user.phone_number}",
        "REMOVE PROFILE",
    ]
    actions = {
        1: lambda: print(prompts.EDIT_NOT_ALLOWED),
        2: lambda: print(prompts.EDIT_NOT_ALLOWED),
        3: lambda: edit_user_detail(user, "first_name", "Enter Your new First Name: "),
        4: lambda: edit_user_detail(user, "last_name", "Enter Your new Last Name: "),
        5: lambda: edit_user_detail(user, "gender", "Select Your new Gender (M/F/O): "),
        6: lambda: edit_user_detail(
            user, "date_of_birth", "Enter Your new Date of Birth(YY-MM-DD): "
        ),
        7: lambda: edit_user_detail(user, "email", "Enter Your new Email: "),
        8: lambda: edit_user_detail(user, "user_password", "Enter Your new Password: "),
        9: lambda: edit_user_detail(
            user, "phone_number", "Enter Your new Phone Number: "
        ),
        10: lambda: edit_user_detail(user, "DELETE"),
    }

    opt = get_user_option(profile_menu, heading)
    if opt in actions:
        actions[opt]()
    else:
        print(prompts.INVALID_INPUT)
