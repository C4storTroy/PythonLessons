import turtle

def draw_square(some_turtle):
    i=0
    while (i<4):
        some_turtle.forward(100)
        some_turtle.left(45)
        some_turtle.forward(100)
        some_turtle.left(135)
        i = i+1

def draw_art():
    window = turtle.Screen()
    window.bgcolor("gray")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    brad.goto(10,10)
    brad.speed(0.5)
    for i in range (1,37):
        draw_square(brad)
        brad.right(10)

    #brad.forward(300)


    brad.goto(-100,-180)


    window.exitonclick()

draw_art()
