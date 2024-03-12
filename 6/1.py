import sqlite3
from tkinter import *

class ConnectDB:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connector = sqlite3.connect(self.db_name)
        self.cursor = self.connector.cursor()

    def SelectSQL(self, sql_text):
        self.sql_text = sql_text
        return  self.cursor.execute(self.sql_text)

class MainWindow:
    def __init__(self, title, size):
        self.window = Tk()
        self.window.geometry(size)
        self.window.resizable(False, False)
        self.window.title(title)
        self.window.configure(bg="#b9faeb")

    def VisibleWindow(self):
        self.window.mainloop()

    def DestroyWindow(self):
        self.window.destroy()

start = MainWindow("ВХОД", "400x400")
start.VisibleWindow()