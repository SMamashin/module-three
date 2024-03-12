import random
from tkinter import *

def click_function(event):
    while True:
        for i in range(16):
            color = random.choice(random_color)
            canvas.itemconfig("ball"+str(i), fill=color)
            canvas.update()
            canvas.after(50)

window = Tk()
window.title("RGB")
window.geometry("500x500")

canvas = Canvas(width=500, height=500, bg="grey")
canvas.pack()

random_color = ['red', 'blue', 'green']

for i in range(16):
    color = random.choice(random_color)
    canvas.create_oval(20+i*30, 50, 40+i*30, 70, fill=color, tags="ball"+str(i))

canvas.create_line(50, 50, 500, 50)
canvas.create_text(250, 150, text="Click to holiday", font="Arial 20", activefill="#ffffff", tags="start")
canvas.tag_bind("start", "<Button-1>", click_function)

window.mainloop()