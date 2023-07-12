import math
import turtle

def xt(t):
    return 16 * math.sin(t) ** 3

def vt(t):
    return 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)

t = turtle.Turtle()
t.speed(50)
turtle.colormode(255)
turtle.Screen().bgcolor(8, 8, 8)
for i in range(2550):
    t.goto((xt(i) * 20, vt(i) * 20))
    red = (255 - i) % 256
    green = i % 256
    blue = (255 - i) % 256
    t.pencolor(red, green, blue)
    t.goto(0, 0)

t.hideturtle()
turtle.update()
turtle.mainloop()
