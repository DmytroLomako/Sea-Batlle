from turtle import *
from enemyships import list_enemy

tracer(0, 0)
speed(0)
hideturtle()
for i in list_enemy:
    print(i)
list_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
list1 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
list2 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

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
button = Turtle()
button.hideturtle()
button.speed(0)
button.penup()
button.goto(-350, -300)
button.pendown()
button.pensize(3)
button.forward(150)
button.left(90)
button.forward(150)
button.left(90)
button.forward(150)
button.left(90)
button.forward(150)
button.left(90)
button.penup()
button.goto(-305, -255)
button.write('UP', font=("Arial", 50, "bold"))
button.goto(-150, -300)
button.pendown()
button.forward(150)
button.left(90)
button.forward(150)
button.left(90)
button.forward(150)
button.left(90)
button.forward(150)
button.left(90)
button.penup()
button.goto(-142, -250)
button.write('RIGHT', font=("Arial", 45, "bold"))
button.pendown()
button.pensize(1)
button_clicked = 0

i = 1
def click(x, y):
    global draw, text1, i, button_clicked, button
    if draw == False:
        if x > -350 and x < -200 and y > -300 and y < -150:
            button_clicked = 1
        elif x >= -150 and x <= 0 and y >= -300 and y <= -150:
            button_clicked = 2
        
        if x >= -350 and x <= -320:
            x = 0
        elif x > -320 and x <= -290:
            x = 1
        elif x > -290 and x <= -260:
            x = 2
        elif x > -260 and x <= -230:
            x = 3
        elif x > -230 and x <= -200:
            x = 4
        elif x > -200 and x <= -170:
            x = 5
        elif x > -170 and x <= -140:
            x = 6
        elif x > -140 and x <= -110:
            x = 7
        elif x > -110 and x <= -80:
            x = 8
        elif x > -80 and x <= -50:
            x = 9
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
        
        if i <= 4:
            if x != None and y != None:
                if list1[x][y] == 0:
                    pensize(3)
                    draw = True
                    list1[x][y] = 1
                    list1[x + 1][y] = 1
                    list1[x - 1][y] = 1
                    list1[x][y + 1] = 1
                    list1[x + 1][y + 1] = 1
                    list1[x - 1][y + 1] = 1  
                    list1[x][y - 1] = 1
                    list1[x + 1][y - 1] = 1
                    list1[x - 1][y - 1] = 1 
                    for o in range(4):
                        penup()
                        goto((x * 30 - 350), (y * -30 + 180))
                        seth(270)
                        pendown()
                        draw_figure(30, 3)
                        draw = False  
                    i += 1
                    if i == 5:
                        text1.clear()
                        text1.write('Arrange 2-deck ships', font=("Arial", 16, "bold"))
        elif i > 4 and i <= 7:
            if button_clicked == 1:             
                if x != None and y != None and y != 0:
                    if list1[x][y] == 0 and list1[x][y - 1] == 0:
                        draw = True
                        list1[x][y] = 1
                        list1[x + 1][y] = 1
                        list1[x - 1][y] = 1
                        list1[x][y + 1] = 1
                        list1[x + 1][y + 1] = 1
                        list1[x - 1][y + 1] = 1
                        list1[x][y - 1] = 1
                        list1[x + 1][y - 1] = 1
                        list1[x - 1][y - 1] = 1
                        list1[x][y - 2] = 1
                        list1[x + 1][y - 2] = 1
                        list1[x - 1][y - 2] = 1
                        for j in range(3):
                            penup()
                            goto((x * 30 - 320), (y * -30 + 150))
                            seth(90)
                            pensize(3)
                            pendown()
                            draw_figure(30, 4)
                            forward(30)
                            left(90)
                            forward(30)
                            right(90)
                            seth(0)
                            draw_figure(30, 3)
                            draw = False
                        i += 1
                        button_clicked = 0
                        if i == 8:
                            text1.clear()
                            text1.write('Arrange 3-deck ships', font=("Arial", 16, "bold"))
            elif button_clicked == 2:
                if x != None and y != None and x != 9:
                    if list1[x][y] == 0 and list1[x + 1][y] == 0:
                        draw = True
                        list1[x][y] = 1
                        list1[x + 1][y] = 1
                        list1[x - 1][y] = 1
                        list1[x][y + 1] = 1
                        list1[x + 1][y + 1] = 1
                        list1[x - 1][y + 1] = 1
                        list1[x][y - 1] = 1
                        list1[x + 1][y - 1] = 1
                        list1[x - 1][y - 1] = 1
                        list1[x + 2][y] = 1
                        list1[x + 2][y - 1] = 1
                        list1[x + 2][y + 1] = 1
                        for p in range(3):
                            penup()
                            goto((x * 30 - 350), (y * -30 + 150))
                            seth(0)
                            pensize(3)
                            pendown()
                            draw_figure(30, 4)
                            seth(0)
                            forward(30)
                            left(90)
                            forward(30)
                            seth(270)
                            draw_figure(30, 3)
                            draw = False
                        i += 1
                        button_clicked = 0
                        if i == 8:
                            text1.clear()
                            text1.write('Arrange 3-deck ships', font=("Arial", 16, "bold"))
        elif i > 7 and i <= 9:
            if button_clicked == 1:
                if x != None and y != None and y != 0:
                    if list1[x][y] == 0 and list1[x][y - 1] == 0 and list1[x][y - 2] == 0:
                        draw = True
                        list1[x][y] = 1
                        list1[x + 1][y] = 1
                        list1[x - 1][y] = 1
                        list1[x][y + 1] = 1
                        list1[x + 1][y + 1] = 1
                        list1[x - 1][y + 1] = 1
                        list1[x][y - 1] = 1
                        list1[x + 1][y - 1] = 1
                        list1[x - 1][y - 1] = 1
                        list1[x][y - 2] = 1
                        list1[x + 1][y - 2] = 1
                        list1[x - 1][y - 2] = 1
                        list1[x][y - 3] = 1
                        list1[x + 1][y - 3] = 1
                        list1[x - 1][y - 3] = 1
                        for j in range(2):
                            penup()
                            goto((x * 30 - 320), (y * -30 + 150))
                            seth(90)
                            pensize(3)
                            pendown()
                            draw_figure(30, 4)
                            forward(30)
                            left(90)
                            forward(30)
                            right(90)
                            seth(0)
                            draw_figure(30, 4)
                            left(90)
                            forward(30)
                            right(90)
                            draw_figure(30, 3)
                            draw = False
                        i += 1
                        button_clicked = 0
                        if i == 10:
                            text1.clear()
                            text1.write('Arrange 4-deck ship', font=("Arial", 16, "bold"))
            if button_clicked == 2:
                if x != None and y != None and x != 9:
                    if list1[x][y] == 0 and list1[x + 1][y] == 0 and list1[x + 2][y] == 0:
                        draw = True
                        list1[x][y] = 1
                        list1[x + 1][y] = 1
                        list1[x - 1][y] = 1
                        list1[x][y + 1] = 1
                        list1[x + 1][y + 1] = 1
                        list1[x - 1][y + 1] = 1
                        list1[x][y - 1] = 1
                        list1[x + 1][y - 1] = 1
                        list1[x - 1][y - 1] = 1
                        list1[x + 2][y] = 1
                        list1[x + 2][y - 1] = 1
                        list1[x + 2][y + 1] = 1
                        list1[x + 3][y] = 1
                        list1[x + 3][y - 1] = 1
                        list1[x + 3][y + 1] = 1
                        for p in range(2):
                            penup()
                            goto((x * 30 - 350), (y * -30 + 150))
                            seth(0)
                            pensize(3)
                            pendown()
                            draw_figure(30, 4)
                            seth(0)
                            forward(30)
                            left(90)
                            forward(30)
                            seth(270)
                            draw_figure(30, 4)
                            left(90)
                            forward(30)
                            right(90)
                            draw_figure(30, 3)
                            draw = False        
                        i += 1
                        button_clicked = 0
                        if i == 10:
                            text1.clear()
                            text1.write('Arrange 4-deck ship', font=("Arial", 16, "bold"))
        elif i == 10:
            if button_clicked == 1:
                if x != None and y != None and y != 0:
                    if list1[x][y] == 0 and list1[x][y - 1] == 0 and list1[x][y - 2] == 0 and list1[x][y - 3] == 0:
                        draw = True
                        list1[x][y] = 1
                        list1[x + 1][y] = 1
                        list1[x - 1][y] = 1
                        list1[x][y + 1] = 1
                        list1[x + 1][y + 1] = 1
                        list1[x - 1][y + 1] = 1
                        list1[x][y - 1] = 1
                        list1[x + 1][y - 1] = 1
                        list1[x - 1][y - 1] = 1
                        list1[x][y - 2] = 1
                        list1[x + 1][y - 2] = 1
                        list1[x - 1][y - 2] = 1
                        list1[x][y - 3] = 1
                        list1[x + 1][y - 3] = 1
                        list1[x - 1][y - 3] = 1
                        list1[x][y - 4] = 1
                        list1[x + 1][y - 4] = 1
                        list1[x - 1][y - 4] = 1
                        for j in range(5):
                            penup()
                            goto((x * 30 - 320), (y * -30 + 150))
                            seth(90)
                            pensize(3)
                            pendown()
                            draw_figure(30, 4)
                            forward(30)
                            left(90)
                            forward(30)
                            right(90)
                            seth(0)
                            draw_figure(30, 4)
                            left(90)
                            forward(30)
                            right(90)
                            draw_figure(30, 4)
                            left(90)
                            forward(30)
                            right(90)
                            draw_figure(30, 3)
                            draw = False
                        i += 1
                        button_clicked = 0
                        button.clear()
                        text1.clear()
            if button_clicked == 2:
                if x != None and y != None and x != 9:
                    if list1[x][y] == 0 and list1[x + 1][y] == 0 and list1[x + 2][y] == 0 and list1[x + 3][y] == 0:
                        draw = True
                        list1[x][y] = 1
                        list1[x + 1][y] = 1
                        list1[x - 1][y] = 1
                        list1[x][y + 1] = 1
                        list1[x + 1][y + 1] = 1
                        list1[x - 1][y + 1] = 1
                        list1[x][y - 1] = 1
                        list1[x + 1][y - 1] = 1
                        list1[x - 1][y - 1] = 1
                        list1[x + 2][y] = 1
                        list1[x + 2][y - 1] = 1
                        list1[x + 2][y + 1] = 1
                        list1[x + 3][y] = 1
                        list1[x + 3][y - 1] = 1
                        list1[x + 3][y + 1] = 1
                        list1[x + 4][y] = 1
                        list1[x + 4][y - 1] = 1
                        list1[x + 4][y + 1] = 1
                        for p in range(5):
                            penup()
                            goto((x * 30 - 350), (y * -30 + 150))
                            seth(0)
                            pensize(3)
                            pendown()
                            draw_figure(30, 4)
                            seth(0)
                            forward(30)
                            left(90)
                            forward(30)
                            seth(270)
                            draw_figure(30, 4)
                            left(90)
                            forward(30)
                            right(90)
                            draw_figure(30, 4)
                            left(90)
                            forward(30)
                            right(90)
                            draw_figure(30, 3)
                            draw = False
                        i += 1
                        button_clicked = 0
                        button.clear()
                        text1.clear()
onscreenclick(click)
            
draw_field(-350, 150)
draw_field(50, 150)
text()
update()
mainloop()