from tkinter import *
from tkinter.ttk import *
from tksheet import Sheet

class Window:
    def __init__(self, geometry="500x500"):
        self.root = Tk()
        self.root.geometry(geometry)

class MainMenu(Window):

    def __init__(self, curs):
        super().__init__()
        self.curs = curs
        Button(self.root, text="View items", command=lambda:ItemMenu(self.curs)).pack()
        Button(self.root, text="View orders", command=lambda:OrderMenu(self.curs)).pack()

class ItemMenu(Window):
    def __init__(self, curs):
        super().__init__()
        itemsTable = Table(self.root)
        itemsTable.fill(curs, "items")

class OrderMenu(Window):
    def __init__(self, curs):
        super().__init__()
        itemsTable = Table(self.root, curs=curs, getHeadersFrom="SELECT * FROM orders INNER JOIN users WHERE orders.uId==users.id")
        itemsTable.fill(curs, "orders", getChildFrom=["users", "uId"], )
        self.curs=curs

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

    def setHeader(self, headers):
        self.headers = [[i for ind, i in enumerate(headers) if not i in headers[:ind]]]
        try:
            self.sheet.config(width=(len(self.headers)*120)+30)
        except Exception as e:
            print(e)

    def __init__(self, root, headers=None, curs=None, getHeadersFrom=None):
        super().__init__(root)
        if getHeadersFrom != None:
            curs.execute(getHeadersFrom)
            self.setHeader([i[0] for i in curs.description])
        else:
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
        # IF STATEMENTS
        if not getChildFrom:
            curs.execute(f"SELECT * FROM {fromTable}")
        else:
            curs.execute(f"SELECT * FROM {fromTable} INNER JOIN {getChildFrom[0]} WHERE {fromTable}.{getChildFrom[1]}=={getChildFrom[0]}.{self.primaryKey}")     
        # IF STATEMENTS END
        curs.execute(f"PRAGMA table_info('{getChildFrom[0]}')")
        self.primaryKey = [i[1] for i in curs.fetchall() if i[-1] == 1][0]
        self.add(curs.fetchall())