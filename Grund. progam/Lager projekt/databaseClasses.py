import sqlite3

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
        self.database.execute(f"SELECT * FROM users WHERE id=={}")
        self.user = self.database.fetchone()
        self.orderID = orderID

def createOrders(database, table="orders"):
    database.execute(f"SELECT * FROM {table}")
    return [Order(database, i[0]) for i in database.fetchall()]