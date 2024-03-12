from tkinter import *

def click_function(event):
    canvas.itemconfig("blue_rect", fill='red')
    canvas.itemconfig("yellow_rect", fill="blue")
    canvas.itemconfig("black_rect", fill="green")

window = Tk()

window.title("Square")
window.geometry("700x700")

canvas = Canvas(width=700, height=700, bg="#f0eee9")
canvas.pack()

rect_1 = canvas.create_rectangle(50, 50, 100, 100, fill="blue", tags=('rect', 'blue_rect'))
rect_2 = canvas.create_rectangle(50, 150, 100, 200, fill="yellow", tags=('rect', 'yellow_rect'))
rect_3 = canvas.create_rectangle(50, 250, 100, 300, fill="black", tags=('rect', 'black_rect'))

canvas.tag_bind('rect', '<Button-1>', click_function)

window.mainloop()