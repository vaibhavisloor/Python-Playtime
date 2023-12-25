from turtle import Turtle,Screen

turtle = Turtle()

turtle.shape("arrow")
turtle.color('black')

# Draw a square
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)


# Draw dashed line
# turtle.penup()
# turtle.backward(300)

# for i in range(0,30):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()

# Drawing multiple figures

turtle.color("blue")

for i in range(0,4):
    turtle.forward(100)
    turtle.right(90)

turtle.color("red")

for i in range(0,5):
    turtle.forward(100)
    turtle.right(72)

turtle.color('green')

for i in range(0,6):
    turtle.forward(100)
    turtle.right(60)

turtle.color('yellow')

for i in range(0,7):
    turtle.forward(100)
    turtle.right(51.4)

turtle.color('orange')

for i in range(0,8):
    turtle.forward(100)
    turtle.right(45)


turtle.color('gray')

for i in range(0,9):
    turtle.forward(100)
    turtle.right(40)    






screen = Screen()
screen.exitonclick()