from turtle import *
from random import *

tracer(0,0)
speed(0)
hideturtle()

list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

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
            

            
def text():
    for i in range(9):
        penup()
        goto(359, (154 - i * 30))
        write(i+1, font=("Arial", 13, "bold"))
    penup()
    goto(354, -116)
    write(10, font=("Arial", 13, "bold"))
    for i in range(9):
        penup()
        goto(-365, (154 - i * 30))
        write(i+1, font=("Arial", 13, "bold"))
    penup()
    goto(-370, -116)
    write(10, font=("Arial", 13, "bold"))
    index = 0
    for i in range(10):
        penup()
        if i == 8:
            goto(304, 183)
            write(list[index], font=("Arial", 13, "bold"))
            index += 1
            continue
        goto((60 + i * 30), 183)
        write(list[index], font=("Arial", 13, "bold"))
        index += 1
    index = 0
    for i in range(10):
        penup()
        if i == 8:
            goto(-96, 183)
            write(list[index], font=("Arial", 13, "bold"))
            index += 1
            continue
        goto((-340 + i * 30), 183)
        write(list[index], font=("Arial", 13, "bold"))
        index += 1
    


def click(x, y):
    print(x, y)
    
onscreenclick(click)
            
draw_field(-350, 150)
draw_field(50, 150)
text()
update()
mainloop()