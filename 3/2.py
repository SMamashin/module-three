import random
from tkinter import *
from tkinter.ttk import Radiobutton

class Ball:
    def __init__(self, canvas):
        self.canvas = canvas
        self.radius = random.randint(15, 35)
        self.x = random.randint(self.radius, 640 - self.radius)
        self.y = random.randint(self.radius, 640 - self.radius)
        self.velX = random.choice([-10, 10, 20, -20])
        self.velY = random.choice([-15, 15, 25, -25])
        self.colors = [
            "#fa1302", "#fa02e9", "#268ded",
            "#16f0e8", "#24f016", "#bdf016",
            "#688509", "#f6ff00", "#ff9900",
            "#eb9fed", "#7c1180", "#0db3bf",
            "#0dbf60", "#9587ed", "#87edb7"
        ]

    def move(self):
        x1, y1, x2, y2 = self.canvas.coords(self.ball)
        if x1 <= 0 or x2 >= 640:
            self.velX *= -1
        if y1 <= 0 or y2 >= 640:
            self.velY *= -1

        self.canvas.move(self.ball, self.velX, self.velY)

    def draw(self):
        self.ball = self.canvas.create_oval(self.x - self.radius, self.y - self.radius,
                                            self.x + self.radius, self.y + self.radius,
                                            fill=self.color)

window = Tk()
window.geometry("640x640")
window.title("Вечеринка с шариками!")
canvas = Canvas(width=640, height=640, bg="grey")
canvas.pack()

balls = []
colors = [
    "#fa1302", "#fa02e9", "#268ded",
    "#16f0e8", "#24f016", "#bdf016",
    "#688509", "#f6ff00", "#ff9900",
    "#eb9fed", "#7c1180", "#0db3bf",
    "#0dbf60", "#9587ed", "#87edb7"
]

for i in range(15):
    if colors:
        color = random.choice(colors)
        colors.remove(color)
    else:
        color = "black"  # Если список цветов пуст, можно использовать другой цвет по умолчанию
    ball = Ball(canvas)
    ball.color = color
    balls.append(ball)

def animate():
    for ball in balls:
        ball.move()
    canvas.after(60, animate)

def draw_balls():
    for ball in balls:
        ball.draw()

draw_balls()
animate()
window.mainloop()