import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "dev",
    passwd = "K1$$100",
)

# prepare a cursor object using cursor() method

cursorObject = dataBase.cursor()

# create the database   

cursorObject.execute("CREATE DATABASE IF NOT EXISTS openstow")

print("Database created successfully ")