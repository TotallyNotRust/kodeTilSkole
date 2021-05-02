import sqlite3 as sql
import uiClasses
import pandas as pd

conn = sql.connect("database.db")
curs = conn.cursor()

curs.execute("""SELECT * FROM orders
                INNER JOIN users ON orders.uId == users.id""")

menu = """
############################################
# Press read to read from database         #
# Press new to add to database             #
# Press rem to remove from table products  #
# Press top to view top selling products   #
############################################"""

def showFromQuery(query):
    table = pd.read_sql_query(query, conn)
    print(table)

def addToDB():
    table = input("What table: ")

    curs.execute(f"PRAGMA table_info({table})")
    primaryKey = [i[1] for i in curs.fetchall() if i[-1] == 1]
    curs.execute(f"PRAGMA foreign_key_list({table})")
    foreignKeys = [[i[3], i[4], i[2]] for i in curs.fetchall()]

    curs.execute(f"SELECT * FROM {table} LIMIT 1")
    columns = curs.description
    aIInt = curs.fetchall()[-1][0] + 1 # auto increment int; assign this to primary key
    values = []
    for i in columns:
        if i[0] in primaryKey:
            values.append(aIInt)
            continue
        value = input(i[0]+": ")
        try:
            values.append(int(value))
        except Exception:
            values.append(value)

    formattedColumns = ", ".join(*columns[1:])
    questionMarks = ", ".join(["?"]*(len(columns)-1))
    print("Kommando: " + f"INSERT INTO {table} VALUES {tuple(i for i in values)}")
    curs.execute(f"INSERT INTO {table} ({formattedColumns}) VALUES ({questionMarks})", (values))  # bruger noget python magi snå en method er kompatibel med alle tables
    #             "INSERT INTO users VALUES ('1', 'Gustav', 'Thomsen', 'Skjoldborgsvej, 22', 'Hjørring', 9800)"
    conn.commit()


def readFromDB():
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