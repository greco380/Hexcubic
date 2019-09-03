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

    turtle.up()
    turtle.right(180)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(50)
    turtle.down()

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

    turtle.up()
    turtle.left(120)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(60)
    turtle.down()

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

    turtle.up()
    turtle.left(180)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(50)
    turtle.down()

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

    turtle.up()
    turtle.right(120)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(30)
    turtle.down()

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

    turtle.up()
    turtle.right(90)
    turtle.forward(40)
    turtle.down()

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

    turtle.up()
    turtle.right(60)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(70)
    turtle.down()

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

    turtle.up()
    turtle.left(120)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(60)
    turtle.down()

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

    turtle.up()
    turtle.left(180)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(90)
    turtle.down()

def I():
    up()

    turtle.begin_fill()
    turtle.left(120)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(20)
    turtle.left(120)
    turtle.forward(20)
    turtle.end_fill()

    turtle.right(180)
    turtle.forward(20)
    turtle.right(90)

    up()

    turtle.up()
    turtle.right(210)
    turtle.forward(130)
    turtle.down()

def J():
    up()

    turtle.begin_fill()
    turtle.left(120)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(20)
    turtle.left(120)
    turtle.forward(20)
    turtle.end_fill()

    turtle.right(180)
    turtle.forward(20)
    turtle.right(90)

    down()

    turtle.up()
    turtle.left(180)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(100)
    turtle.down()

def K():
    up()

    turtle.begin_fill()
    turtle.left(120)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(20)
    turtle.left(120)
    turtle.forward(20)
    turtle.end_fill()

    turtle.left(60)
    turtle.forward(40)
    turtle.left(90)

    down()

    turtle.up()
    turtle.right(60)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(70)
    turtle.down()

def L():
    up()

    turtle.begin_fill()
    turtle.left(120)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(20)
    turtle.left(120)
    turtle.forward(20)
    turtle.end_fill()

    turtle.left(60)
    turtle.forward(40)
    turtle.left(90)

    up()

def M():
    down()

    turtle.begin_fill()
    turtle.right(120)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(20)
    turtle.end_fill()

    turtle.right(180)
    turtle.forward(40)
    turtle.left(90)

    up()

    turtle.up()
    turtle.left(60)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(60)
    turtle.down()

def N():
    down()

    turtle.begin_fill()
    turtle.right(120)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(20)
    turtle.end_fill()

    turtle.right(180)
    turtle.forward(40)
    turtle.left(90)

    down()

    turtle.up()
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(60)
    turtle.down()

def O():
    down()

    turtle.right(120)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(20)
    turtle.begin_fill()
    turtle.right(60)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(20)
    turtle.end_fill()
    turtle.right(90)

    down()

    turtle.up()
    turtle.left(180)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(40)
    turtle.down()

def P():
    down()

    turtle.right(120)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(20)
    turtle.begin_fill()
    turtle.right(60)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(20)
    turtle.end_fill()
    turtle.right(90)

    up()

    turtle.up()
    turtle.left(240)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(30)
    turtle.down()

def Q():
    down()

    turtle.right(120)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(20)
    turtle.begin_fill()
    turtle.right(60)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(20)
    turtle.end_fill()
    turtle.right(120)
    turtle.forward(20)
    turtle.right(30)

    up()

    turtle.up()
    turtle.left(120)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(40)
    turtle.down()

def R():
    down()

    turtle.right(120)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(20)
    turtle.begin_fill()
    turtle.right(60)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(20)
    turtle.end_fill()
    turtle.right(120)
    turtle.forward(20)
    turtle.right(30)

    down()

def S():
    down()

def T():
    down()

def U():
    down()

def V():
    down()

def W():
    down()

def X():
    down()

def Y():
    empty()

def Z():
    empty()


turtle.up()
turtle.left(90)
turtle.forward(100)
turtle.down()
turtle.left(90)
turtle.forward(500)
turtle.right(180)
#turtle.down()

def A_L():
    A()
    B()
    C()
    D()
    E()
    F()
    turtle.forward(500)
    turtle.right(180)
    turtle.forward(600)
    turtle.right(180)
    turtle.forward(100)
    G()
    H()
    I()
    J()
    K()
    L()
    turtle.up()
    turtle.forward(200)
    turtle.down()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(180)
    turtle.forward(1100)
    turtle.right(180)

A_L()
O()
P()
Q()
R()

turtle.done()
