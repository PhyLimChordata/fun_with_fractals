import turtle

# drawer set up
loadWindow = turtle.Screen()
loadWindow.screensize(1000,1000)
drawer = turtle.Pen()
drawer.speed(100)
drawer.penup()
drawer.goto(-300, 100)
drawer.pendown()


# defining our function that draws +
def draw_fractal(length, depth):
    drawer.forward(length)
    if depth > 1:
        drawer.backward(length / 2)
        drawer.left(90)
        draw_fractal(length/1.6, depth - 1)
        drawer.right(180)
        draw_fractal(length/1.6, depth - 1)
        drawer.right(90)
        drawer.forward(length / 2)
    drawer.right(180)
    drawer.forward(length)


draw_fractal(300, 10)
drawer.right(180)
draw_fractal(300, 10)

turtle.done()
