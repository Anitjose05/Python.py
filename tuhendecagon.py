import turtle
hex=turtle.Turtle()
turtle.bgcolor("yellow")
hex.fillcolor("cyan")
hex.begin_fill()
for i in range(11):
    hex.forward(50)
    hex.left(32.73)
hex.end_fill()
turtle.done()
