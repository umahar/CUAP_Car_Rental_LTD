"""stores all common prompts/headings"""

DASHES = " ------------ "
WELCOME = f"\n{DASHES}WELCOME TO CUAP CAR RENTAL{DASHES}\n"
EXIT = f"\n{DASHES}Thanks for using CUAP Car Rental services. Exiting{DASHES}\n"
INVALID_INPUT = f"\n{DASHES}ERROR: INVALID INPUT{DASHES}\n"
STANDARD_MENU = "Choose an option from the Menu"
DB_ERROR = " --------------- DB ERROR: {} --------------- "
DATA_LOADING_FAILED = f"\n{DASHES}ERROR: DATA LOADING FAILED{DASHES}\n"
LOGIN_SUCCESS = f"\n{DASHES}LOGIN SUCCESSFUL{DASHES}\n"
LOGIN_FAILED = (
    f"\n{DASHES}ERROR: Unknown email/password. "
    f"Please recheck your email and password{DASHES}\n"
)
REGISTER_FAILED = (
    f"\n{DASHES}ERROR: An account already exists"
    f" with that email. Please login{DASHES}\n"
)
REGISTER_SUCCESS = f"\n{DASHES}REGISTRATION SUCCESSFUL{DASHES}\n"
UNKNOWN_ERROR = (
    f"\n{DASHES}ERROR: An unknown error has occurred. Please contact support.{DASHES}\n"
)
LOGOUT = f"\n{DASHES}SUCCESSFULLY LOGGED OUT{DASHES}\n"
WELCOME_LOGIN_TEXT = "\n{}Welcome {} {}{}\n"
MY_DETAILS = f"\n{DASHES}LOADING DETAILS{DASHES}\n"
EDIT_DETAILS = f"\n{DASHES}EDIT DETAILS{DASHES}\n"
UPDATE_SUCCESSFUL = f"\n{DASHES}PROFILE UPDATE SUCCESSFUL{DASHES}\n"
EDIT_NOT_ALLOWED = (
    f"\n{DASHES}ERROR:You can not edit this detail."
    f" Please contact admin support.{DASHES}\n"
)
VIEW_NOTIFICATIONS = f"\n{DASHES}VIEW YOUR ACCOUNT NOTIFICATIONS{DASHES}\n"
NO_NOTIFICATIONS = f"\n{DASHES}ERROR:Account has no notifications yet.{DASHES}\n"
SELECT_NOTIFICATION = "\nSelect a Notification to view its details:"
NOTIFICATION_HEADING = "\nNo.       Notification ID   \t Date      Type"
NOTIFICATION_DETAILS = f"\n{DASHES}NOTIFICATION DETAILS{DASHES}\n"
NOTIFICATIONS_DELETED = f"\n{DASHES}ALL NOTIFICATIONS DELETED{DASHES}\n"
UNREAD_NOTIFICATIONS = (
    "\nYou have {} unread notifications. View notifications by pressing '9'.\n"
)
CAR_ADDED = f"\n{DASHES}CAR REGISTRATION SUCCESSFUL{DASHES}\n"
INVALID_USERNAME = f"\n{DASHES}ERROR: USERNAME ALREADY EXISTS. TRY AGAIN{DASHES}\n"
INVALID_EMAIL = f"\n{DASHES}ERROR: EMAIL ALREADY EXISTS. TRY AGAIN{DASHES}\n"
