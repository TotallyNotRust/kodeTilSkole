from tkinter import *
from tkinter.ttk import *
from tksheet import Sheet

class Window:
    def __init__(self, geometry="500x500"):
        self.root = Tk()
        self.root.geometry(geometry)

class MainMenu(Window):
    def test(self):
        print("Hi")
    def __init__(self, curs):
        super().__init__()
        self.curs = curs
        Button(self.root, text="Say hi!", command=lambda:ItemMenu(self.curs)).pack()
        Button(self.root, text="Say hi!", command=lambda:OrderMenu(self.curs)).pack()

class ItemMenu(Window):
    def __init__(self, curs):
        super().__init__()
        itemsTable = Table(self.root)
        itemsTable.fill(curs, "items")

class OrderMenu(Window):
    def __init__(self, curs):
        itemsTable = Table(self.root, ["oId", "address", "city", "firstname"])
        itemsTable.fill(curs, "orders", getChildFrom={"uid": "users"}, )

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

    def __init__(self, root, headers=["id", "name", "price", "stock"]):
        super().__init__(root)
        self.headers = headers
        self.sheet = Sheet(root, width=(len(self.headers)*120)+30, show_x_scrollbar=False, headers=self.headers)
        self.sheet.grid(row=0,column=0, columnspan=3)
        self.root = root
    
    def fill(self, 
            curs, 
            fromTable, 
            conditions = None,
            getChildFrom = None, 
            ):
        curs.execute(f"SELECT * FROM {fromTable}")
        print()
        values = {i: j for i, j in zip(curs.description, curs.fetchall())}
        self.add()
        if getChildFrom:
            for i in values:
                for j in getChildFrom:
                    curs.execute(f"SELECT * FROM {getChildFrom[j]} where {j}=={values[i]}")
                    self.add(curs.fetchall())

