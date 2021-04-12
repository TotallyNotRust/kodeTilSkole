from tkinter import *
from tkinter.ttk import *
from tksheet import Sheet

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
    
    def fill(self, curs, fromTable, conditions = None):
        curs.execute(f"SELECT * FROM {fromTable}")
        self.add(curs.fetchall())

class Item:
    def __init__(self, name, id, price):
        self.iId = id
        self.name = name
        self.price = float(price)

class OrderLine:
    def __init__(self, values, parent):
        self.orderLineId = values[0]
        self.itemId = values[1]
        parent.database.execute(f"SELECT * FROM items WHERE id=={self.itemId}")
        name, id, price, _ = parent.database.fetchone()
        self.item = Item(name, id, price)
        self.parent = parent


class Order:
    def __init__(self, database, orderID, orderlineTable="orderLines"):
        self.database = database
        self.database.execute(f"SELECT * FROM {orderlineTable} WHERE oId=={orderID}")
        self.orderLines = [OrderLine(i, self) for i in database.fetchall()]
        self.orderID = orderID

def createOrders(database, table="orders"):
    database.execute(f"SELECT * FROM {table}")
    return [Order(database, i[0]) for i in database.fetchall()]