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
        itemsTable.fill(curs, "orders", getChildFrom=["users", "uId"], )

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
            self.sheet.headers, self.headers = [curs.description]*2 # Ganger listen med 2 så den indeholder curs.description 2 gang; det gøres fordi den skal sætte curs.description ind i to variabler
            self.sheet.config(width=(len(self.headers)*120)+30)
            curs.execute(f"SELECT * FROM {fromTable}")
            self.add(curs.fetchall())
        else:
            curs.execute(f"SELECT * FROM {fromTable} INNER JOIN {getChildFrom[0]} WHERE {fromTable}.{getChildFrom[1]}=={getChildFrom[0]}.{getChildFrom[1]}")
                    


