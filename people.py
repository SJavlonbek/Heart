import turtle
from sketchpy import canvas

obj = canvas.sketchpy_from_svg("ben10.svg")
t = turtle.Turtle()
t.penup()
t.pendown()
obj.draw()
