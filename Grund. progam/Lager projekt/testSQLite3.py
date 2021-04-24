import sqlite3 as sql
import uiClasses

conn = sql.connect("database.db")
curs = conn.cursor()

curs.execute("""SELECT * FROM orders
                INNER JOIN users ON orders.uId == users.id""")

menu = """
#################################
# Press r to read from database #
# Press n to add to database    #
#################################"""

def addToDB():
    table = input("What table: ")

    curs.execute(f"PRAGMA table_info('{table}')")
    primaryKey = [i[1] for i in curs.fetchall() if i[-1] == 1]

    curs.execute(f"SELECT * FROM {table}")
    columns = curs.description
    aIInt = len(curs.fetchall()) + 1 # auto increment int; assign this to primary key
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
    questionMarks = ",".join(["?"]*len(columns))
    print("Kommando: " + f"INSERT INTO {table} VALUES ({questionMarks})", (values))
    curs.execute(f"INSERT INTO {table} VALUES ({questionMarks})", (values))  # bruger noget python magi så en method er kompatibel med alle tables
    #             "INSER INTO users VALUES (1, 'Gustav', 'Thomsen', 'Skjoldborgsvej, 22', 'Hjørring', 9800)"
    conn.commit()

def readFromDB():
    table = input("Table: ")
    curs.execute(f"SELECT * FROM {table}")
    print(list([x[0] for x in curs.description]))
    for ind, i in enumerate(curs.fetchall()):
        print("   |   ".join(str(j) for j in i))

while True:
    print(menu, end=None)
    x = input(": ")
    if x == "n":
        addToDB()
    elif x == "r":
        readFromDB()