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

def F():
    down()

def G():
    up()

def H():
    down()

def I():
    up()

def J():
    down()

def K():
    up()

def L():
    down()

def space_between():
    turtle.up()
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.down()


A()
space_between()
B()
space_between()
C()
space_between()
D()
turtle.done()
