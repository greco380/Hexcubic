'''
This program draws two hexagon diagrams which are offset
60 degrees from each other.
August 30, 2019
By: Josh Greco
'''
#The turtle module is needed
import turtle

turtle.speed()

def draw_hexagon():
    """
    This function draws a single hexagon.
    Preconditions: The turtle is is positioned to draw
        the bottom of the hexagon from left to right
    Postconditions: the turtle ends on the right side of
        the bottom of the hexagon and is turns 60 degrees
        to begin drawing the next hexagon.
        The pen is down.
    """
    turtle.forward(50)
    turtle.left(60)
    turtle.forward(50)
    turtle.left(60)
    turtle.forward(50)
    turtle.left(60)
    turtle.forward(50)
    turtle.left(60)
    turtle.forward(50)
    turtle.left(60)
    turtle.forward(50)
    turtle.left(60)
    turtle.forward(50)
    turtle.right(60)

def six_hexagons():
    """
    This function draws all 6 of the hexagons of the first layer.
    :preconditions: The turtle is is positioned to draw
        the bottom of the first hexagon from left to right
    :postconditions: the turtle ends where it started having drawn
        all 6 hexagons needed for the first secotion of the program.
        The pen is down.
    """
    draw_hexagon()
    draw_hexagon()
    draw_hexagon()
    draw_hexagon()
    draw_hexagon()
    draw_hexagon()
    turtle.right(60)

six_hexagons() #This calls the function to draw the first layer of hexagons
turtle.pencolor('red') #This changes the pen color to red so that the user can tell a differencebetween the two layers
six_hexagons() #This calls the function to draw the second layer of hexagons
turtle.pencolor('black') #This changes the pen back to black
turtle.left(60) #This positions turtle so that it can end in the same position as the video

