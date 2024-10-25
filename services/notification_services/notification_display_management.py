"""handles the logic to display notifications for any user"""

from data import prompts
from services.notification_services.notification import (
    delete_notifications,
    get_all_notifications,
)
from utils.get_user_option import get_user_option


def display_notifications(user_id):
    """shows any type of notifications based on user id and filters"""
    print(prompts.VIEW_NOTIFICATIONS)
    main_notification_menu = [
        "All Notifications",
        "Unread Notifications",
        "Notifications by Category",
        "Delete all Notification",
    ]
    notification_categories = [
        "Account/Profile",
        "Rentals & Bookings",
        "Payments",
        "Admin Support Ticket",
    ]
    sorting_menu = ["Sort By Date: ASC", "Sort By Date: DES"]
    opt = get_user_option(main_notification_menu, prompts.STANDARD_MENU)
    if opt == 1:
        sort = get_user_option(sorting_menu, prompts.STANDARD_MENU)
        if sort != 0:
            display_all_notifications(user_id, sort)
    if opt == 2:
        sort = get_user_option(
            sorting_menu, "Select your sorting for the notifications"
        )
        if sort != 0:
            display_unread_notifications(user_id, sort)
    if opt == 3:
        category = get_user_option(
            notification_categories, "Select a category for the notifications"
        )
        if category != 0:
            sort = get_user_option(
                sorting_menu, "Select your sorting for the notifications"
            )
            if sort != 0:
                display_notifications_by_category(user_id, sort, category)
    if opt == 4:
        delete_all_notifications(user_id)


def display_all_notifications(user_id, sort):
    """displays all notifications based on selected asc or des sort"""
    sort_by = ""
    if sort == 1:
        sort_by = "ASC"
    if sort == 2:
        sort_by = "DESC"
    notifications = get_all_notifications(user_id, sort_by)
    if notifications:
        print_notifications(notifications)
    else:
        print(prompts.NO_NOTIFICATIONS)


def display_unread_notifications(user_id, sort):
    """displays all notifications based on selected asc or des sort"""


def display_notifications_by_category(user_id, sort, category):
    """displays all notifications based on selected asc or des sort"""


def delete_all_notifications(user_id):
    """deletes all notifications"""
    print("\nType 'DELETE' to remove all Notifications. THIS CAN NOT BE UNDONE.\n")
    res = input("RESPONSE: ")
    if res == "DELETE":
        if delete_notifications(user_id):
            print(prompts.NOTIFICATIONS_DELETED)
        else:
            print(prompts.UNKNOWN_ERROR)
    else:
        print(prompts.INVALID_INPUT)


def print_notifications(notifications):
    """This function formats and prints notifications."""
    # Define column headers
    headers = ["Sr#", "Notification Type", "Message", "Date", "Time"]
    # Define column widths
    col_widths = [5, 20, 20, 12, 10]

    # Print headers with formatting
    header_row = f"{headers[0].ljust(col_widths[0])} {headers[1].ljust(col_widths[1])} {headers[2].ljust(col_widths[2])} {headers[3].ljust(col_widths[3])} {headers[4].ljust(col_widths[4])}"
    print(header_row)
    print("-" * len(header_row))

    # Print each notification with formatting
    for index, item in enumerate(notifications):
        # Ensure item[3] (datetime) is treated as a string
        date_time_str = str(item[4])
        date_part = date_time_str[:10]  # First 10 characters for the date
        time_part = date_time_str[11:]  # Characters after the 11th for the time

        # Format and print each row
        row = f"{str(index+1).ljust(col_widths[0])} {str(item[5]).ljust(col_widths[1])} {str(item[2]).ljust(col_widths[2])} {date_part.ljust(col_widths[3])} {time_part.ljust(col_widths[4])}"
        print(row)

    print()
