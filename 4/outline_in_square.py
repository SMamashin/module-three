import os
from tkinter import *

def update_status():
    sova_coords = canvas.coords(sova)
    if (home_coords[0] < sova_coords[0] < home_coords[2]) and (home_coords[1] < sova_coords[1] < home_coords[3]):
        status_label.config(text="Сова в доме")
    else:
        status_label.config(text="Сова за пределами дома")

def move(event):
    key = event.keysym
    if key =="Up":
        canvas.move(sova,0,-10)
    elif key == "Down":
        canvas.move(sova,0,10)
    elif key == "Left":
        canvas.move(sova, -10, 0)
    elif key == "Right":
        canvas.move(sova, 10, 0)
    update_status()

window = Tk()
window.geometry("600x600")

status_label = Label(window, text="", font=("Arial", 16))
status_label.pack(side="bottom")
canvas = Canvas(window, width=600, height=600, bg="lightblue")
canvas.pack()
# branch = PhotoImage("branch.png")
# home = canvas.create_image(0, 0, image=branch)
home = canvas.create_oval(225, 225, 450, 450, width=2)
image = PhotoImage(file="img.png").subsample(5)
sova = canvas.create_image(300,300,image=image)

# coords
home_coords = canvas.coords(home)
sova_coords = canvas.coords(sova)
print(home_coords, sova_coords)

window.bind("<KeyPress>",move)

window.mainloop()