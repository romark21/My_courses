def turttle() -> None:
    import turtle
    turtle.shape("turtle")
    turtle.shapesize(2)
    turtle.color('blue', 'yellow')
    turtle.speed(10)



    def zvezda():

        turtle.begin_fill()
                #for i in range(8):
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(100)
        turtle.right(120)
        turtle.forward(40)
        turtle.left(60)
        turtle.forward(40)
        turtle.right(120)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(60)
        turtle.forward(70)
        turtle.right(120)
        turtle.forward(70)
        turtle.left(60)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(200)
        turtle.end_fill()

        turtle.penup()
        turtle.goto(200, 0)
        turtle.pendown()

        turtle.begin_fill()
        turtle.left(90)
        turtle.forward(50)
        turtle.left(75)
        turtle.forward(50)
        turtle.right(75)
        turtle.forward(50)
        turtle.right(75)
        turtle.forward(50)
        turtle.left(75)
        turtle.forward(50)
        turtle.left(110)
        turtle.forward(200)
        turtle.left(70)
        turtle.forward(40)
        turtle.left(70)
        turtle.forward(200)


        turtle.end_fill()




    zvezda()
    turtle.done()
#turttle()


def mnogougolnik():
    import turtle
    polygon = turtle.Turtle()
    num_sides = 6
    side_length = 100
    angle = 360.0 / num_sides

    for i in range(num_sides):
        polygon.forward(side_length)
        polygon.right(angle)

    turtle.exitonclick()
#mnogougolnik()



def risunok_zvezda():
    import turtle

    spiral = turtle.Turtle()
    spiral.color('red')
    spiral.pensize(1)
    spiral.speed(10.2)
    for i in range(80):
        spiral.forward(i * 10)
        spiral.right(144)
    turtle.exitonclick()

#risunok_zvezda()


def pjati_kone4naja_zvezda_i_kvdrat():
    import turtle
    turtle.shape("turtle")
    turtle.color("green", "red")
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(150)
        turtle.left(144)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(200, 0)
    turtle.pendown()
    turtle.color("green", "yellow")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-160, 0)
    turtle.pendown()
    turtle.color("red", "blue")
    turtle.begin_fill()
    for i in range(9):
        turtle.forward(152)
        turtle.left(160)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-320, 0)
    turtle.pendown()
    turtle.color("red", "blue")
    turtle.begin_fill()
    for i in range(8):
        turtle.forward(100)
        turtle.right(135)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-160, 150)
    turtle.pendown()
    turtle.color("red", "blue")
    turtle.begin_fill()
    for i in range(9):
        turtle.forward(100)
        turtle.left(140)
        turtle.forward(100)
        turtle.right(100)

    turtle.end_fill()


    turtle.exitonclick()
pjati_kone4naja_zvezda_i_kvdrat()

