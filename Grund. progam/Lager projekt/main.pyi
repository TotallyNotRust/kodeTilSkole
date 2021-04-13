from tkinter import *
from tkinter.ttk import *
from tksheet import Sheet
import sqlite3
"""Import classes"""
from databaseClasses import *
from uiClasses import *

conn = sqlite3.connect("database.db") ## Conn = connection
curs = conn.cursor() ## Curs = curser

root = MainMenu(curs) # Laver et vindue

orders = createOrders(curs)

root.root.mainloop()