import mysql.connector

mydb = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password = "agwanda",
    database = "mysqldbc"
)
my_cursor = mydb.cursor()

my_cursor.execute("SHOW TABLES")

for x in my_cursor:
    print(x)