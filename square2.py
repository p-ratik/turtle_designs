import turtle as tl
import random as rd
main=tl.Turtle()
screen=tl.Screen()
screen.bgcolor("black")
main.hideturtle()
main.speed(0)

for i in range(1,451):
    r=rd.randint(0,255)
    g=rd.randint(0,255)
    b=rd.randint(0,255)

    tl.colormode(255)
    main.pencolor(r,g,b)
    main.forward(60+i)
    main.right(91)

tl.exitonclick()




