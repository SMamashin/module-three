from tkinter import *

def move(event):
    x = event.x
    y = event.y

    wall_x1,wall_y1,wall_x2,wall_y2, = canvas.coords(wall)
    if x < wall_x1:
        x = wall_x1
    elif x > wall_x2:
        x = wall_x2
    if y < wall_y1:
        y = wall_y1
    elif y > wall_y2:
        y = wall_y2
    print(canvas.coords(wall))
    print("x = ", x, "y = ",y)
    canvas.coords(ball,x - 25, y - 25, x + 25, y + 25)



window = Tk()
window.geometry("600x600")
window.title("Шары")
canvas = Canvas(window, width=600, height=600, bg = "#222222")
canvas.pack()

wall = canvas.create_rectangle(220, 220, 440, 440, fill="pink")
ball = canvas.create_oval(50,50,100,100,fill = "#40e3f5")

canvas.bind("<Motion>",move)

window.mainloop()