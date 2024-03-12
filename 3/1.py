import random
from tkinter import *

window = Tk()
canvas = Canvas(width= 640, height= 640, bg = "grey")
canvas.pack()

def moveBall():
    global vx, vy
    x1, y1, x2, y2 = canvas.coords(my_ball)
    if x1 <= 1 or x2 >= 640:
        vx *= -1
    if x1 <= 1 or x2 >= 640:
        vy *= -1

    canvas.move(my_ball,vx,vy )
    canvas.after(65,moveBall)

vx = random.choice([-10,10,20,-20])
vy = random.choice([-15,15,25,-25])

my_ball = canvas.create_oval(300,300,350,350,fill = "pink")




moveBall()
window.mainloop()