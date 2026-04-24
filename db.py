import mysql.connector
from credentials import *

connection = mysql.connector.connect(
    host = my_host,
    user = my_user,
    password = my_password,
    database = my_database
)

cursor = connection.cursor()

