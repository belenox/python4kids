import turtle
t = turtle.Pen()
draw = "yes"
def somefunc(x):
    global draw
    if x == "yes":
        draw = "no"
        t.up()
    elif x == "no":
        draw = "yes"
        t.down()
    else:
        draw = "no"
        t.up()
def turtlefunc():
    z = raw_input("[W, A, S, D, E]")
    if z == "w":
        t.forward(25)
    if z == "s":
        t.backward(25)
    if z == "a":
        t.left(45)
    if z == "d":
        t.right(45)
    if z == "quit":
        quit()
    if z == "q":
        somefunc(draw)
    turtlefunc()
turtlefunc()
