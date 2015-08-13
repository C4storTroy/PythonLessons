import turtle

#that function receive 5 parameters
def draw_square(some_turtle,x,y,d1,d2,color):
    i=0
    while (i<4):
        some_turtle.forward(d1)
        some_turtle.left(x)
        some_turtle.forward(d2)
        some_turtle.left(y)
        some_turtle.color(color)
        i = i+1

def draw_art():
    window = turtle.Screen()
    window.bgcolor("gray")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.goto(10,10)
    brad.speed(0.5)
    for i in range (1,37):
        draw_square(brad,135,45,100,100,"blue")
        brad.right(10)

    #brad.forward(300)


    brad.color("brown")
    brad.goto(0,0)
    brad.right(90)
    brad.forward(200)
    draw_square(brad,225,-45,50,50,"green")



    window.exitonclick()

draw_art()
