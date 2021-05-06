import sqlite3 as sql
import uiClasses
import pandas as pd

conn = sql.connect("database.db")
curs = conn.cursor()

curs.execute("PRAGMA foreign_keys = ON;")

menu = """
############################################
# Press read to read from database         #
# Press new to add to database             #
# Press rem to remove from table products  #
# Press top to view top selling products   #
############################################"""

def showFromQuery(query):
    try:
        table = pd.read_sql_query(query, conn)
        print(table)
    except Exception as e:
        print(e)

def addToDB():
    while True:
        table = input("What table: ")
        try:
            curs.execute(f"PRAGMA table_info({table})")
            primaryKey = [i[1] for i in curs.fetchall() if i[-1] == 1]

            curs.execute(f"SELECT * FROM {table} LIMIT 1")
            columns = [i[0] for i in curs.description if not i[0] in primaryKey]
            break
        except Exception:
            continue
    
    values = []
    for i in columns:
        value = input(i+": ")

        values.append(value)

    formattedColumns = ", ".join(columns)
    questionMarks = ", ".join(["?"]*(len(columns)))
    print("Kommando: " + f"INSERT INTO {table} VALUES {tuple(i for i in values)}")
    try:
        curs.execute(f"INSERT INTO {table} ({formattedColumns}) VALUES ({questionMarks})", (values))  # bruger noget python magi snå en method er kompatibel med alle tables
        conn.commit()
    except Exception as e:
        print("\nOne of the entered values is not valid: ")
        print(e)


def readFromDB():
    con.commit()
    table = input("Table: ")
    showFromQuery(f"SELECT * FROM {table}")

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

def getTable(table):
    curs.execute(f"PRAGMA table_info({table})")
    return curs.fetchall()

def removeItem():
    query = f"""
        DELETE FROM {(table:= input('Table to remove from: '))} 
        WHERE 
        {(primaryKey:=[i[1] for i in getTable(table) if i[-1] == 1][0])} 
        == 
        {input(f'{primaryKey} of object to remove: ')
        }"""
    curs.execute(query)
    conn.commit()

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