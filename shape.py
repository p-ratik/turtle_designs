import turtle as tl
import random as rd
main=tl.Turtle()
screen=tl.Screen()
screen.bgcolor("black")
main.hideturtle()
#l=["purple","red",'orange','blue','green']
l=["red","orange","yellow","green","cyan","purple"]
main.speed(0)
for i in range(300):
    # main.color(l[i%6])
    r=rd.randint(0,255)
    g=rd.randint(0,255)
    b=rd.randint(0,255)
    tl.colormode(255)
    main.pencolor(r,g,b)
    main.pensize(i/40+1)
    main.forward(i)
    main.right(59)
tl.done()
