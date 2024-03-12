from tkinter import *

def move(event):
    #Получаем координаты объекта
    x, y = event.x, event.y
    print("x= ", x, "y", y)
    canvas.coords(ball,x - 25, y - 25, x + 25, y + 25 )

window = Tk()
window.geometry("400x400")

canvas = Canvas(window,width=400, height=400, bg="green")
canvas.pack()

ball = canvas.create_oval(50,50,100,100,fill = "black")

#Привязываем событие "движение мыши" к функции move

canvas.bind("<Motion>",move)

window.mainloop()