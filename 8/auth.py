import sqlite3
from tkinter import *
from tkinter import messagebox

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

    def StartWidget(self):
        self.lable_title = MyLabel("ВХОД", "Arial 20 bold", "#b9faeb", 150, 50)
        self.label_login = MyLabel("ЛОГИН:", "Arial 15", "#b9faeb", 50, 150)
        self.label_password = MyLabel("ПАРОЛЬ: ", "Arial 15", "#b9faeb", 50, 200)
        self.entry_login = MyEntry("Arial 15", 150, 150, 150, False)
        self.entry_password = MyEntry("Arial 15", 150, 200, 150, True)
        self.entry_password_entry = self.entry_password.entry
        self.enter_btn = MyButton("ВХОД", "Arial 15", 150, 300, 100, self, "enter")
        self.show_btn = MyButton("☼", "Arial 12", 310, 200, 35, self, "show")

    def canva_for_work_window(self):
        self.canva = Canvas(width=800, height=800, bg="#b9faeb")
        self.canva.pack()
        self.work_place = self.canva.create_rectangle(500, 100, 650, 300, width=3, dash=(1, 1))
        self.start_place = self.canva.create_rectangle(500, 590, 650, 790, width=3, dash=(1, 1))
        self.txt_master = self.canva.create_text(600, 320, font="Arial 15", text="Мастерская")
        self.txt_garage = self.canva.create_text(600, 570, font="Arial 15", text="Гараж")
class MyLabel:
    def __init__(self, text, font, bg, x, y):
        self.label = Label(text=text, font=font, bg=bg)
        self.label.place(x=x, y=y)

class MyEntry:
    def __init__(self, font, x, y, width, mask):
        self.value = StringVar()
        if mask == True:
            show = "*"
        else:
            show = ""

        self.entry = Entry(textvariable=self.value, font=font, show=show)
        self.entry.place(x=x, y=y, width=width)

class MyButton:
    def __init__(self, text, font, x, y, width, window, command):
        self.window = window
        self.command = command
        self.button = Button(text=text, font=font, activebackground="blue", activeforeground="white")
        self.button.place(x=x, y=y, width=width)
        self.button.bind("<Button-1>", lambda event: self.click(self.command))

    def click(self, command):
        if command == "enter":
            self.enter()
        elif command == "show":
            self.show()

    def show(self):
        if self.window.entry_password_entry.cget('show') == '':
            self.window.entry_password_entry.config(show='*')
        else:
            self.window.entry_password_entry.config(show='')
    def enter(self):
        self.value_login = self.window.entry_login.value.get()
        self.value_pass = self.window.entry_password.value.get()

        self.db = ConnectDB('db.db')

        self.sql = self.db.SelectSQL("SELECT * from users")

        for row in self.sql:
            self.db_login = row[1]
            self.db_pass = row[2]

            if self.value_login == self.db_login and self.value_pass == self.db_pass:
                self.open = True
                break
            else:
                self.open = False

        # self.db.close_db()

        if self.open:
            messagebox.showinfo("Внимание!", "Доступ разрешен")
            self.window.DestroyWindow()
            self.work_window = MainWindow("Сервисный центр", "800x800")
            self.work_window.canva_for_work_window()
            self.work_window.VisibleWindow()
        else:
            messagebox.showerror("Внимание!", "Неверный логин или пароль")

start = MainWindow("ВХОД", "400x400")
start.StartWidget()
start.VisibleWindow()