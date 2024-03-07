from turtle import *


speed(100)
# Create a new turtle screen and set its background color
screen = Screen()
screen.bgcolor("skyblue")







#draw the sun

sun = Turtle()
sun.hideturtle()
sun.penup()
sun.goto(300, 300)
sun.pendown()
sun.color("yellow")
sun.begin_fill()
sun.circle(50)
sun.end_fill()
sun.speed(30)

#we want to paint a house

speed(30)
#step1:draw a square
width(7)
color("red")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door 

forward(70)
color("blue")
begin_fill()
left(90)
forward(120)     #hight of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("black")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(200, 200)


width(7)
color("black")
pendown()
penup()
goto(-200, 5)
pendown()
left(120)
forward(-150)

#we want to paint a house

speed(30)
#step1:draw a square
width(7)
color("red")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door 

forward(70)
color("blue")
begin_fill()
left(90)
forward(120)     #hight of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(600, 200)
pendown()

color("black")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(200, 200)



width(7)
color("black")
pendown()
penup()
goto(-200, 5)
pendown()
left(120)
forward(-500)

#we want to paint a house

speed(30)
#step1:draw a square
width(7)
color("red")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door 

forward(70)
color("blue")
begin_fill()
left(90)
forward(120)     #hight of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(-150, 200)
pendown()

color("black")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(200, 200)



width(7)
color("black")
pendown()
penup()
goto(-200, 5)
pendown()
left(120)
forward(600)

#we want to paint a house

speed(30)
#step1:draw a square
width(7)
color("red")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door 

forward(70)
color("blue")
begin_fill()
left(90)
forward(120)     #hight of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(-500, 200)
pendown()

color("black")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(200, 200)

width(50)
color("brown")
pendown()
penup()
goto(-75, 0)
pendown()
left(210)
forward(100)

sun = Turtle()
sun.hideturtle()
sun.penup()
sun.goto(-75, 50)
sun.pendown()
sun.color("green")
sun.begin_fill()
sun.circle(50)
sun.end_fill()
sun.speed(30)

sun = Turtle()
sun.hideturtle()
sun.penup()
sun.goto(-75, 125)
sun.pendown()
sun.color("green")
sun.begin_fill()
sun.circle(50)
sun.end_fill()
sun.speed(30)


width(50)
color("brown")
pendown()
penup()
goto(-425, 0)
pendown()
left(0)
forward(100)

sun = Turtle()
sun.hideturtle()
sun.penup()
sun.goto(-425, 50)
sun.pendown()
sun.color("green")
sun.begin_fill()
sun.circle(50)
sun.end_fill()
sun.speed(30)

sun = Turtle()
sun.hideturtle()
sun.penup()
sun.goto(-425, 125)
sun.pendown()
sun.color("green")
sun.begin_fill()
sun.circle(50)
sun.end_fill()
sun.speed(30)



width(50)
color("brown")
pendown()
penup()
goto(300, 0)
pendown()
left(0)
forward(100)

sun = Turtle()
sun.hideturtle()
sun.penup()
sun.goto(300, 50)
sun.pendown()
sun.color("green")
sun.begin_fill()
sun.circle(50)
sun.end_fill()
sun.speed(30)

sun = Turtle()
sun.hideturtle()
sun.penup()
sun.goto(300, 125)
sun.pendown()
sun.color("green")
sun.begin_fill()
sun.circle(50)
sun.end_fill()
sun.speed(30)


width(50)
color("brown")
pendown()
penup()
goto(675, 0)
pendown()
left(0)
forward(100)

sun = Turtle()
sun.hideturtle()
sun.penup()
sun.goto(675, 50)
sun.pendown()
sun.color("green")
sun.begin_fill()
sun.circle(50)
sun.end_fill()
sun.speed(30)

sun = Turtle()
sun.hideturtle()
sun.penup()
sun.goto(675, 125)
sun.pendown()
sun.color("green")
sun.begin_fill()
sun.circle(50)
sun.end_fill()
sun.speed(30)




exitonclick()
