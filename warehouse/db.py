import sqlite3 as sql

def connectDB():
    con = sql.connect("warehouse.db")
    return con