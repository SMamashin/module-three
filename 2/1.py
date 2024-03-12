import random
from tkinter import *

def move_ball_1():
    step = random.randint(1, 20)
    canvas.move(ball_1, step, 0)
    if canvas.coords(ball_1)[2] < 500:
        canvas.after(50, move_ball_1)

window = Tk()

window.geometry("600x600")
window.title("Outline")

canvas = Canvas(width=600, height=600, bg="grey")
canvas.pack()

ball_1 = canvas.create_oval(50, 50, 100, 100, fill="red")
move_ball_1()

window.mainloop()

