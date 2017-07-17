import turtle
t = turtle.Pen()
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
    if z == "e":
        t.down()
    if z == "q":
        t.up()
    if z == "quit":
        quit()
    if z == "toggle":
        print draw
        if draw == "yes":
            draw = "no"
            t.up()
        elif draw == "no":
            draw = "yes"
            t.down()
        else:
            draw = "no"
            t.up()
    turtlefunc()
turtlefunc()
