#the authors' names are Cadyn and Sarah
import turtle
tom = turtle.Turtle()
tom.color("yellow")

for side in range(4):
    if side == 1:
        tom.color("red")
    if side == 2:
        tom.color("purple")
    tom.forward(100)
    tom.right(90)
