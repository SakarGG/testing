# TO CREATE SQLITE DATABASE TABLES
import sqlite3

conn = sqlite3.connect("db.sqlite")
cursor = conn.cursor()

# Visitor
sql_query = """CREATE TABLE IF NOT EXISTS Visitor (
    id integer PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    address text NOT NULL,
    city text NOT NULL, 
    phoneNumber text,
    email text,
    device_ID text,
    infected INTEGER
    )"""
cursor.execute(sql_query)

# Place
sql_query = """CREATE TABLE IF NOT EXISTS Place (
    id integer PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    address text NOT NULL,
    phoneNumber text,
    email text
    )"""
cursor.execute(sql_query)

# Agent
sql_query = """CREATE TABLE IF NOT EXISTS Agent (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username text UNIQUE NOT NULL,
    password text NOT NULL
    )"""
cursor.execute(sql_query)

# Hopsital
sql_query = """CREATE TABLE IF NOT EXISTS Hospital (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    username text NOT NULL UNIQUE,
    password text NOT NULL
    )"""
cursor.execute(sql_query)
