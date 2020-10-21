import turtle as tl
import random as rd
main=tl.Turtle()
screen=tl.Screen()
screen.bgcolor("black")
main.hideturtle()
main.speed(0)

l=["red","orange","yellow","green","cyan","purple"]

main.color("cyan")
for i in range(120):
    main.pensize(3)
    #main.color(l[i%6])
    r=rd.randint(0,255)
    g=rd.randint(0,255)
    b=rd.randint(0,255)
    tl.colormode(255)
    main.pencolor(r,g,b)
    for i in range(3):
        main.forward(170)
        main.left(90)
    main.forward(170)
    main.left(93)




tl.done()
