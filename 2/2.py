import random
from tkinter import *
from tkinter import messagebox

def start():
    for ball in balls:
        step = random.randint(1, 20)
        canvas.move(ball, step, 0)
        if canvas.coords(ball)[2] >= 500:
            winner_color = canvas.itemcget(ball, 'fill')
            messagebox.showinfo('Победитель', f"Выйграл: {winner_color}")
            return
    canvas.after(50, start)

def again():
    for ball_2 in balls_2:
        step = random.randint(1, 25)
        canvas.move(ball_2, step, 0)
        if canvas.coords(ball_2)[2] >= 500:
            winner_color = canvas.itemcget(ball_2, 'fill')
            messagebox.showinfo('Победитель', f"Выйграл: {winner_color}")
            return
    canvas.after(50, again)

window = Tk()
window.geometry("500x500")
window.title("Need for Speed")

canvas = Canvas(width=500, height=500, bg="grey")
canvas.pack()

balls = [
    canvas.create_oval(50, 50, 100, 100, fill="red"),
    canvas.create_oval(50, 150, 100, 200, fill="green"),
    canvas.create_oval(50, 250, 100, 300, fill="blue"),
    canvas.create_oval(50, 350, 100, 400, fill="white")
]

balls_2 = [
    canvas.create_oval(50, 50, 100, 100, fill="yellow"),
    canvas.create_oval(50, 150, 100, 200, fill="pink"),
    canvas.create_oval(50, 250, 100, 300, fill="orange"),
    canvas.create_oval(50, 350, 100, 400, fill="black")
]

btn_start = Button(text="начать", font="Arial 15", command=start)
btn_start.place(x=400, y=25)
btn_again = Button(text="заново", font="Arial 13", command=again)
btn_again.place(x=400, y=80)

window.mainloop()
