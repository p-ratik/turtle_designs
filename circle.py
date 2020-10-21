import turtle as tl
import random as rd
main=tl.Turtle()
screen=tl.Screen()
screen.bgcolor("black")
main.hideturtle()
main.pensize(2)
main.speed(0)
colors=["red","orange","yellow","green","cyan"]
for i in range(38):
    #main.color(colors[i%5])
    r=rd.randint(0,255)
    g=rd.randint(0,255)
    b=rd.randint(0,255)
    tl.colormode(255)
    main.pencolor(r,g,b)
    main.circle(100)
    main.right(10)
tl.done()
