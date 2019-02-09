import turtle

# drawer
loadWindow = turtle.Screen()
loadWindow.screensize(1000,1000)
drawer = turtle.Pen()
drawer.speed(100)
drawer.penup()
# picks up the pen (not to draw anything)
drawer.goto(-300, 100)
# the pen goes to this location with the
drawer.pendown()
# the pen is now down so it can draw now


# defining our function that draws +
def draw_fractal(length, depth):
    drawer.forward(length)
    if depth > 1:
        drawer.backward(length / 2)
        # after drawing forward goes to the midpoint of the line
        drawer.left(90)
        # rotates the drawer (does the top part of +)
        draw_fractal(length/1.6, depth - 1)
        # recursively draws more crosshairs off the branching crosshair
        drawer.right(180)
        draw_fractal(length/1.6, depth - 1)
        drawer.right(90)
        drawer.forward(length / 2)
        # goes back to original position
    drawer.right(180)
    drawer.forward(length)


draw_fractal(300, 10)
drawer.right(180)
draw_fractal(300, 10)

turtle.exitonclick()
