"""authenticates a user based on email and password"""

from mysql.connector import Error
from config.db_connection import create_connection
from data import prompts, users_queries
