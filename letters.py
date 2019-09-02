import turtle

turtle.speed(0)


def up():
    turtle.right(30)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(20)

    turtle.left(180)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(20)
    turtle.left(180)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(20)

def down():
    turtle.right(30)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(20)

    turtle.right(240)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(20)
    turtle.left(180)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(20)

def empty():
    turtle.right(30)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(20)



def A():
    up()

    turtle.begin_fill()
    turtle.right(120)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(20)
    turtle.end_fill()

    turtle.right(60)
    turtle.forward(20)
    turtle.right(90)

    up()

def B():
    up()

    turtle.begin_fill()
    turtle.right(120)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(20)
    turtle.end_fill()

    turtle.right(60)
    turtle.forward(20)
    turtle.right(90)

    down()

def C():
    up()

    turtle.begin_fill()
    turtle.right(120)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(20)
    turtle.end_fill()

    turtle.right(120)
    turtle.forward(20)
    turtle.right(90)

    down()

def D():
    up()

    turtle.begin_fill()
    turtle.right(120)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(20)
    turtle.end_fill()

    turtle.right(120)
    turtle.forward(20)
    turtle.right(90)

    up()

def E():
    up()
    turtle.right(120)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(20)

    turtle.begin_fill()
    turtle.right(120)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(20)
    turtle.left(120)
    turtle.forward(20)
    turtle.end_fill()

    turtle.right(60)
    turtle.forward(20)
    turtle.left(90)

    up()

def F():
    up()
    turtle.right(120)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(20)

    turtle.begin_fill()
    turtle.right(120)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(20)
    turtle.left(120)
    turtle.forward(20)
    turtle.end_fill()

    turtle.right(60)
    turtle.forward(20)
    turtle.left(90)

    down()

def G():
    up()
    turtle.right(120)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(20)

    turtle.begin_fill()
    turtle.right(120)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(20)
    turtle.left(120)
    turtle.forward(20)
    turtle.end_fill()

    turtle.right(150)

    down()

def H():
    up()
    turtle.right(120)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(20)

    turtle.begin_fill()
    turtle.right(120)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(20)
    turtle.left(120)
    turtle.forward(20)
    turtle.end_fill()

    turtle.right(150)

    up()

def I():
    up()

def J():
    down()

def K():
    up()

def L():
    down()

def space_between_up():
    turtle.up()
    turtle.right(180)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(50)
    turtle.down()

def space_between_down():
    turtle.up()
    turtle.left(120)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.down()

turtle.up()
turtle.left(180)
turtle.forward(500)
turtle.right(180)
turtle.down()
A()
space_between_up()
B()
space_between_down()
C()
space_between_up()
D()
space_between_down()
E()
space_between_up()
F()
space_between_down()
G()
space_between_up()
H()
space_between_down()

turtle.done()
