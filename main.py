from turtle import *
from random import *

speed(0)
hideturtle()

def draw_figure(size, count):
    for i in range(count):
        forward(size)
        left(360/count)
    
def draw_field(x, y):
    penup()
    goto(x, y)
    pendown()
    for i in range(10):
        penup()
        goto(x, y-30*i)
        pendown()
        for j in range(10):
            draw_figure(30, 4)
            forward(30)

def click(x, y):
    print(x, y)
    
onscreenclick(click)
            
draw_field(-400, 150)
draw_field(100, 150)

mainloop()