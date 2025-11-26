import sqlite3 

#variables 
CONN = sqlite3.connect("school.db")
CURSOR = CONN.cursor()