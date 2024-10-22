"""all queries of users table"""

ADD_USER = """
INSERT INTO users(
    username, user_role, first_name, last_name,gender,date_of_birth, email, user_password, phone_number
    ) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
"""

GET_ALL_USERS = """SELECT * from users;"""

GET_USER_PASSWORD_BY_EMAIL = """SELECT user_password from users WHERE email = %s;"""

GET_USER_DATA_BY_ID = """SELECT * from users where user_id = %s;"""

GET_USER_ID_BY_EMAIL = """SELECT user_id from users where email = %s;"""

GET_USER_BY_EMAIL = """SELECT * from users where email = %s;"""

GET_USER_BY_USERNAME = """SELECT * from users where username = %s;"""

DELETE_USER = """DELETE FROM users WHERE username = %s;"""
