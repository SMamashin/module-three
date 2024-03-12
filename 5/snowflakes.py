import random
from tkinter import *

class Snowflake:
    def __init__(self, canvas, img):
        self.canvas = canvas
        self.size = random.randint(5, 15)
        self.x = random.randint(self.size, 600 - self.size)
        self.y = random.randint(self.size, 600 - self.size)
        self.speed = random.randint(1, 5)
        self.img = PhotoImage(file=img).subsample(10)
        self.shape = canvas.create_image(self.x, self.y, anchor=NW, image=self.img)

    def move(self):
        self.y += self.speed
        self.canvas.move(self.shape, 0, self.speed)

class Snowfall:
    def __init__(self, w):
        self.w = w
        self.canvas = Canvas(w, width=600, height=600, bg="#8a82ba")
        self.canvas.pack()
        self.snowflakes = []

        for _ in range(50):
            snowflake = Snowflake(self.canvas, "./source/snowflake.png")
            self.snowflakes.append(snowflake)

    def animate(self):
        for flake in self.snowflakes:
            flake.move()
            if flake.y > 600:
                flake.y = 0
                flake.x = random.randint(flake.size, 600 - flake.size)
                self.canvas.coords(flake.shape, flake.x, flake.y)
        self.w.after(30, self.animate)

w = Tk()
w.geometry("600x600")
w.title("СНЕГОПАААААД")
w.iconbitmap("./source/favicon.ico")
snowfall = Snowfall(w)
snowfall.animate()
w.mainloop()