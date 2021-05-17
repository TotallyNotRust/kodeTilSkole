import sqlite3 as sql
import pandas as pd
import unittest

# Åbner databasen
conn = sql.connect("database.db")
curs = conn.cursor()

# Slår foreign-key restriction til
curs.execute("PRAGMA foreign_keys = ON;")

# Tester
class Tests(unittest.TestCase):
    def Tests(self):
        self.assertEqual(len(getTable("users")), 6) # Tablet users har 6 columns, derfor skulle den returne en 6 lang list
        self.assertEqual(len(getTable("orders")), 2) # Og orders er 2 lang
        print("Completed tests")

# Definere menu variable med en nemt print-bar string
menu = """
############################################
# Press read to read from database         #
# Press new to add to database             #
# Press rem to remove from table           #
# Press edit to edit from table            #
# Press top to view top selling products   #
############################################"""

# Hviser data fra en query som brugeren passer
def showFromQuery(query):
    try:
        # Loader data og skriver det ud fra det query brugeren har passed
        table = pd.read_sql_query(query, conn)
        print(table)
    except Exception as e:
        # Hvis brugeren har passed et ugyldigt query fejler den, hvis den gpr det skal den udskrive fejlen
        print(e)

# Tilføjer til databasen
def addToDB():
    # Uendeligt loop
    while True:
        # Spørger brugeren om et table
        table = input("What table: ")
        try:
            # Henter primary key fra tablet
            curs.execute(f"PRAGMA table_info({table})")
            primaryKey = [i[1] for i in curs.fetchall() if i[-1] == 1]

            # Henter columns fra tablet
            curs.execute(f"SELECT * FROM {table} LIMIT 1")
            columns = [i[0] for i in curs.description if not i[0] in primaryKey]
            # Hvis alt det kører breaker den det unendelige loop
            break
        except Exception as e:
            # Hvis det fejler printer den det til brugeren
            print(e)
            continue
    
    values = []
    # Looper gennem columns og får bruger input
    for i in columns:
        value = input(i+": ")
        values.append(value)

    # Constructer og kører sql kommando
    formattedColumns = ", ".join(columns)
    questionMarks = ", ".join(["?"]*(len(columns)))
    print("Kommando: " + f"INSERT INTO {table} VALUES {tuple(i for i in values)}")
    try:
        curs.execute(f"INSERT INTO {table} ({formattedColumns}) VALUES ({questionMarks})", (values))  # bruger noget python magi snå en method er kompatibel med alle tables
        conn.commit()
    except Exception as e:
        # Hvis nogen af brugerens input ikke er rigtige vil kommandoen fejle
        print("\nOne of the entered values is not valid: ")
        print(e)

# Tag bruger input og kør metode til at printe et table
def readFromDB():
    conn.commit()
    table = input("Table: ")
    showFromQuery(f"SELECT * FROM {table}")

# Bruger præ sat query (🤮) til at printe alle items ordret efter  
def getTopSold():
    query = """
    SELECT 
        orderLines.iId, 
        items.name as name, 
        COUNT(*) AS amount

    FROM orderLines
        LEFT JOIN items 
            WHERE items.id == orderLines.iId
        GROUP BY orderLines.iId
    """
    showFromQuery(query)

# Får table information ved hjælp PRAGMA 
def getTable(table):
    curs.execute(f"PRAGMA table_info({table})")
    return curs.fetchall()

# Fjerner fra et table
def removeItem():
    # Bruger noget python magi til at tage inputs til stringen, det er nok ikke clean code men det virker hurtigt.
    query = f""" 
        DELETE FROM {(table:= input('Table to remove from: '))} 
        WHERE 
        {(primaryKey:=[i[1] for i in getTable(table) if i[-1] == 1][0])} 
        == 
        {input(f'{primaryKey} of object to remove: ')
        }"""
    # Kører query'en
    curs.execute(query)
    conn.commit()

# Redigere item fra table
def editItem():
    table = input("Please enter a table: ")

    # Lambda funktion brugt til formatering
    formatt = lambda i: input(f"{i}: ")

    # Loader og formatere data
    tableInfo = getTable(table)
    primaryKey = [i[1] for i in tableInfo if i[-1] == 1]
    columns = [i[1] for i in tableInfo if not i[1] in primaryKey]
    formattedSets = ", ".join([f"{i}={formatt(i)}" for i in columns])
    # Kører sql kommando
    conn.execute(f"""
        UPDATE {table} SET 
        {formattedSets}
        WHERE 
        {(primaryKey:=[i[1] for i in getTable(table) if i[-1] == 1][0])} 
        == 
        {input(f'{primaryKey} of object to edit: ')}""")

#Kører tests
tests = Tests()
tests.Tests()
# Tager bruger input.
while True:
    print(menu, end=None)
    x = input(": ")
    if x == "new":
        addToDB()
    elif x == "read":
        readFromDB()
    elif x == "top":
        getTopSold()
    elif x == "rem":
        removeItem()
    elif x == "edit":
        editItem()