"""handles the logic to display notifications for any user"""

from data import prompts
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
            display_all_notifications(sort)
    if opt == 2:
        sort = get_user_option(
            sorting_menu, "Select your sorting for the notifications"
        )
        if sort != 0:
            display_unread_notifications(sort)
    if opt == 3:
        category = get_user_option(
            notification_categories, "Select a category for the notifications"
        )
        if category != 0:
            sort = get_user_option(
                sorting_menu, "Select your sorting for the notifications"
            )
            if sort != 0:
                display_notifications_by_category(sort, category)
    if opt == 4:
        delete_all_notifications()


def display_all_notifications(sort):
    """displays all notifications based on selected asc or des sort"""


def display_unread_notifications(sort):
    """displays all notifications based on selected asc or des sort"""


def display_notifications_by_category(sort, category):
    """displays all notifications based on selected asc or des sort"""


def delete_all_notifications():
    """deletes all notifications"""
