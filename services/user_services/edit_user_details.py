"""edits a given user detail"""

import os
import sys
from data import prompts
from services.user_services.delete_user import delete_user


def edit_user_detail(user, item_to_edit, prompt=""):
    """edits allowed detail"""
    if item_to_edit == "DELETE":
        manage_delete(user.username)


def manage_delete(username):
    """handles delete user"""
    print("\nType 'DELETE' to remove the profile. THIS CAN NOT BE UNDONE.\n")
    res = input("RESPONSE: ")
    if res == "DELETE":
        if delete_user(username):
            print(prompts.USER_DELETED)
            print(prompts.LOGOUT)
            python = sys.executable
            os.execv(python, [python] + sys.argv)
        else:
            print(prompts.UNKNOWN_ERROR)
    else:
        print(prompts.INVALID_INPUT)
