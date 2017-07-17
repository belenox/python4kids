import turtle
turtle.up()
turtle.left(90)
turtle.forward(200)
turtle.right(90)
turtle.down()
def shape():
    x = 0
    while x >= 0:
        x = x + 2
        turtle.forward(x ** 0.7)
        turtle.right(x / 1.5)
        turtle.backward(x ** 0.5)
        turtle.left(x / 2)
shape()
turtle.exitonclick()
