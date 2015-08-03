import turtle

def draw_window():
    window = turtle.Screen()
    window.bgcolor("gray")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    brad.speed(0.5)
    for i in range (1,370):
        draw_square(brad)
        brad.right(1)
    window.exitonclick()

def draw_square(some_turtle):
    i=0
    while (i<4):
        some_turtle.forward(100)
        some_turtle.right(90)
        i = i+1




draw_window()
