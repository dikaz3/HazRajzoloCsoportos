import turtle

i = 0

while i < 4:
    turtle.forward(100)
    turtle.right(90)
    i+=1
i=0
while i<1:
    turtle.setheading(45)
    turtle.forward(70)
    turtle.setheading(-45)
    turtle.forward(70)
    i+=1

turtle.done()