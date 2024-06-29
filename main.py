from turtle import *
from random import *

tracer(0, 0)
speed(0)
hideturtle()

list_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
list1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list6 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list8 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list9 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list10 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

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
        goto(35, (154 - i * 30))
        write(i+1, font=("Arial", 13, "bold"))
    penup()
    goto(30, -116)
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
            write(list_letters[index], font=("Arial", 13, "bold"))
            index += 1
            continue
        goto((60 + i * 30), 183)
        write(list_letters[index], font=("Arial", 13, "bold"))
        index += 1
    index = 0
    for i in range(10):
        penup()
        if i == 8:
            goto(-96, 183)
            write(list_letters[index], font=("Arial", 13, "bold"))
            index += 1
            continue
        goto((-340 + i * 30), 183)
        write(list_letters[index], font=("Arial", 13, "bold"))
        index += 1

draw = False
text1 = Turtle()
text1.hideturtle()
text1.speed(0)
text1.penup()
text1.goto(-300, 230)
text1.write('Arrange 1-deck ships', font=("Arial", 16, "bold"))

def click(x, y):
    global draw, text1
    if draw == False:
        if x >= -350 and x <= -320:
            x = 0
            list = list1
        elif x > -320 and x <= -290:
            x = 1
            list = list2
        elif x > -290 and x <= -260:
            x = 2
            list = list3
        elif x > -260 and x <= -230:
            x = 3
            list = list4
        elif x > -230 and x <= -200:
            x = 4
            list = list5
        elif x > -200 and x <= -170:
            x = 5
            list = list6
        elif x > -170 and x <= -140:
            x = 6
            list = list7
        elif x > -140 and x <= -110:
            x = 7
            list = list8
        elif x > -110 and x <= -80:
            x = 8
            list = list9
        elif x > -80 and x <= -50:
            x = 9
            list = list10
        else:
            x = None
        if y <= 180 and y >= 150:
            y = 0
        elif y < 150 and y >= 120:
            y = 1
        elif y < 120 and y >= 90:
            y = 2
        elif y < 90 and y >= 60:
            y = 3
        elif y < 60 and y >= 30:
            y = 4
        elif y < 30 and y >= 0:
            y = 5
        elif y < 0 and y >= -30:
            y = 6
        elif y < -30 and y >= -60:
            y = 7
        elif y < -60 and y >= -90:
            y = 8
        elif y < -90 and y >= -120:
            y = 9
        else:
            y = None
        if x!= None and y!= None:
            index = y
            if list[index] == 0:
                draw = True
                list[index] = 1
                for i in range(4):
                    penup()
                    goto((x * 30 - 350), (y * -30 + 150))
                    pendown()
                    draw_figure(30, 3)
                    draw = False               

onscreenclick(click)
            
draw_field(-350, 150)
draw_field(50, 150)
text()
update()
mainloop()