import turtle

def draw_window():
    window = turtle.Screen()
    window.bgcolor("gray")
    draw_square()
    draw_circle()
    draw_triangle()
    window.exitonclick()

def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    brad.speed(0.5)
    i=0
    while (i<4):
        brad.forward(100)
        brad.right(90)
        i = i+1


def draw_circle():
    angie = turtle.Turtle()
    angie.color("blue")
    angie.shape("arrow")
    angie.circle(100)

def draw_triangle():
    tri = turtle.Turtle()
    tri.color("green")
    tri.shape("triangle")
    for i in range(0,3):
        tri.backward(100)
        tri.right(-120)

draw_window()
