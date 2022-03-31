import mysql.connector

db = mysql.connector.connect(
    host = 'academia.c1mebdhdxytu.us-east-1.rds.amazonaws.com',
    user = 'p2',
    password = 'ALrUBIaLYcHR',
    database = 'p2',
    port = '3306'
)
db.autocommit = True