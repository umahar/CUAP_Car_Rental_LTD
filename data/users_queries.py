"""all queries of users table"""

ADD_USER = """
INSERT INTO users(
    username, user_role, first_name, last_name,gender,date_of_birth, email, user_password, phone_number
    ) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
"""

GET_ALL_USERS = """SELECT * from users;"""
