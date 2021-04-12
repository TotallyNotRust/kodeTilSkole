from tkinter import *
from tkinter.ttk import *
from tksheet import Sheet
from classes import *
import sqlite3

conn = sqlite3.connect("database.db") ## Conn = connection
curs = conn.cursor() ## Curs = curser

root = Tk() # Laver et vindue

root.geometry("500x500")

table = Table(root)

table.fill(curs, "items")

orders = createOrders(curs)

root.mainloop()