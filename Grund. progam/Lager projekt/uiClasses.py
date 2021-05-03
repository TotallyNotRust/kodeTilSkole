from tkinter import *
from tkinter.ttk import *
from tksheet import Sheet
import sqlite3

class Window:
    def __init__(self, geometry="500x500"):
        self.root = Tk()
        self.root.geometry(geometry)

class AddToDBWindow(Window):
    def __init__(self, columns: list, table, curs = None, database = "database.db"):
        super().__init__()
        self.columns = columns
        if not curs:
            self.database = sqlite3.connect(database)
            self.curs = self.database.cursor()
        else:
            self.curs = curs
        self.entries = []

        for ind, i in enumerate(columns):
            Label(self.root, text=i).grid(row=ind, column=0)
            entry = Entry(self.root)
            self.entries.append(entry)
            entry.grid(row=ind, column = 1)

        Button(self.root, text="Færdig").grid(row=len(self.entries))
            
    def add(self, table, variables):
        questionMarks = ",".join(["?"]*len(self.columns))
        self.curs.execute(f"INSER INTO {table} VALUES ({questionMarks})", variables)

class MainMenu(Window):
    def test(self):
        print("Hi") 
    def __init__(self, curs):
        super().__init__()
        self.curs = curs
        Button(self.root, text="Se alle varer", command=lambda:ItemMenu(self.curs)).pack()
        Button(self.root, text="Se alle ordrer", command=lambda:OrderMenu(self.curs)).pack()
        Button(self.root, text="Se alle ordrer", command=lambda:AddToDBWindow(self.curs, "orders")).pack()

class ItemMenu(Window):
    def __init__(self, curs):
        super().__init__()
        itemsTable = Table(self.root)
        itemsTable.fill(curs, "items")

class OrderMenu(Window):
    def __init__(self, curs):
        super().__init__()
        itemsTable = Table(self.root, ["oId", "address", "city", "firstname"])
        itemsTable.fill(curs, "orders", getChildFrom=["users", "uId", "id"], )

class newOrder(AddToDBWindow):
    def __init__():
        super().__init__()


class CustomTkObject:
    def __add__(self, *kw):
        raise NotImplementedError()

    def __sub__(self):
        raise NotImplementedError()

    def __init__(self, root: Tk):
        self.remove = self.__sub__
        self.add = self.__add__
        self.root = root

class Table(CustomTkObject):
    def __add__(self, toAdd):
        for i in toAdd:
            self.sheet.insert_row(i)

    def __init__(self, root, headers=None):
        super().__init__(root)
        self.headers = headers
        self.sheet = Sheet(root, width=(len(self.headers)*120)+30 if headers != None else 200, show_x_scrollbar=False, headers=self.headers if headers else [])
        self.sheet.grid(row=0,column=0, columnspan=3)
        self.root = root
    
    def fill(self, 
            curs, 
            fromTable, 
            conditions = None,
            getChildFrom = None, 
            ):

        if not getChildFrom:
            curs.execute(f"SELECT * FROM {fromTable}")
            headers = curs.description
        else:
            curs.execute(f"SELECT * FROM {fromTable} INNER JOIN {getChildFrom[0]} WHERE {fromTable}.{getChildFrom[1]}=={getChildFrom[0]}.{getChildFrom[2]}")
            headers = curs.description
        self.headers = tuple(i[0] for i in headers)
        self.sheet.headers(newheaders=self.headers)
        self.sheet.config(width=(len(self.headers)*120)+30)
        self.add(curs.fetchall())
        pass       


