import turtle

# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("white")

# Create a new turtle object
my_turtle = turtle.Turtle()

# Draw the first circle
my_turtle.circle(50)

# Move the turtle to a new position without drawing anything
my_turtle.penup()
my_turtle.forward(100)
my_turtle.pendown()

# Draw the second circle
my_turtle.circle(50)

# Move the turtle to a new position without drawing anything
my_turtle.penup()
my_turtle.backward(50)
my_turtle.left(90)
my_turtle.forward(150)
my_turtle.right(90)
my_turtle.pendown()

# Draw the oval
my_turtle.shape("circle")
my_turtle.shapesize(8, 4,  0)  # Stretch the circle shape to create an oval
my_turtle.stamp()  # Stamp the oval shape onto the screen

# Hide the turtle and keep the screen open until it is clicked
my_turtle.hideturtle()
screen.exitonclick()