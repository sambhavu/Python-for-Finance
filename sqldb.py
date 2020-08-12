#!/usr/bin/python

import MySQLdb


db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database version is ", data)

db.close() 


