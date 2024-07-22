from random import *

list2 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

w1 = 0
w2 = 0
w3 = 0
w4 = 0
def draw_ship1():
    global w1
    while w1 < 4:
        r1 = randint(1, 10)
        r2 = randint(1, 10)
        if list2[r1][r2] == 0:
                list2[r1][r2] = 2
                list2[r1][r2 - 1] = 1
                list2[r1][r2 + 1] = 1
                list2[r1 + 1][r2] = 1
                list2[r1 + 1][r2 - 1] = 1
                list2[r1 + 1][r2 + 1] = 1
                list2[r1 - 1][r2] = 1
                list2[r1 - 1][r2 - 1] = 1
                list2[r1 - 1][r2 + 1] = 1
                w1 += 1
def draw_ship2():
    global w2
    while w2 < 3:
        r1 = randint(1, 10)
        r2 = randint(1, 10)
        r3 = randint(0, 1)
        if r3 == 0: # up
            if r1 != 1:
                if list2[r1][r2] == 0 and list2[r1 - 1][r2] == 0:
                        list2[r1][r2] = 2
                        list2[r1][r2 - 1] = 1
                        list2[r1][r2 + 1] = 1
                        list2[r1 + 1][r2] = 1
                        list2[r1 + 1][r2 - 1] = 1
                        list2[r1 + 1][r2 + 1] = 1
                        list2[r1 - 1][r2] = 2
                        list2[r1 - 1][r2 - 1] = 1
                        list2[r1 - 1][r2 + 1] = 1
                        list2[r1 - 2][r2] = 1
                        list2[r1 - 2][r2 - 1] = 1
                        list2[r1 - 2][r2 + 1] = 1
                        w2 += 1
        elif r3 == 1: # right
            if r2 != 10:
                if list2[r1][r2] == 0 and list2[r1][r2 + 1] == 0:
                    list2[r1][r2] = 2
                    list2[r1][r2 - 1] = 1
                    list2[r1][r2 + 1] = 2
                    list2[r1][r2 + 2] = 1
                    list2[r1 - 1][r2] = 1
                    list2[r1 - 1][r2 - 1] = 1
                    list2[r1 - 1][r2 + 1] = 1
                    list2[r1 - 1][r2 + 2] = 1
                    list2[r1 + 1][r2] = 1
                    list2[r1 + 1][r2 - 1] = 1
                    list2[r1 + 1][r2 + 1] = 1
                    list2[r1 + 1][r2 + 2] = 1
                    w2 += 1
def draw_ship3():
    global w3
    while w3 < 2:
        r1 = randint(1, 10)
        r2 = randint(1, 10)
        r3 = randint(0, 1)
        if r3 == 0: # up
            if r1 != 1 and r1 != 2:
                if list2[r1][r2] == 0 and list2[r1 - 1][r2] == 0 and list2[r1 - 2][r2] == 0:
                    list2[r1][r2] = 2
                    list2[r1][r2 - 1] = 1
                    list2[r1][r2 + 1] = 1
                    list2[r1 + 1][r2] = 1
                    list2[r1 + 1][r2 - 1] = 1
                    list2[r1 + 1][r2 + 1] = 1
                    list2[r1 - 1][r2] = 2
                    list2[r1 - 1][r2 - 1] = 1
                    list2[r1 - 1][r2 + 1] = 1
                    list2[r1 - 2][r2] = 2
                    list2[r1 - 2][r2 - 1] = 1
                    list2[r1 - 2][r2 + 1] = 1
                    list2[r1 - 3][r2] = 1
                    list2[r1 - 3][r2 - 1] = 1
                    list2[r1 - 3][r2 + 1] = 1
                    w3 += 1
        elif r3 == 1: # right
            if r2 != 10 and r2 != 9:
                if list2[r1][r2] == 0 and list2[r1][r2 + 1] == 0 and list2[r1][r2 + 2] == 0:
                    list2[r1][r2] = 2
                    list2[r1][r2 - 1] = 1
                    list2[r1][r2 + 1] = 2
                    list2[r1][r2 + 2] = 2
                    list2[r1][r2 + 3] = 1
                    list2[r1 - 1][r2] = 1
                    list2[r1 - 1][r2 - 1] = 1
                    list2[r1 - 1][r2 + 1] = 1
                    list2[r1 - 1][r2 + 2] = 1
                    list2[r1 - 1][r2 + 3] = 1
                    list2[r1 + 1][r2] = 1
                    list2[r1 + 1][r2 - 1] = 1
                    list2[r1 + 1][r2 + 1] = 1
                    list2[r1 + 1][r2 + 2] = 1
                    list2[r1 + 1][r2 + 3] = 1
                    w3 += 1 
def draw_ship4():
    global w4
    while w4 < 1:
        r1 = randint(1, 10)
        r2 = randint(1, 10)
        r3 = randint(0, 1)
        if r3 == 0: # up
            if r1 != 1 and r1 != 2 and r1 != 3:
                if list2[r1][r2] == 0 and list2[r1 - 1][r2] == 0 and list2[r1 - 2][r2] == 0 and list2[r1 - 3][r2] == 0:
                    list2[r1][r2] = 2
                    list2[r1 - 1][r2] = 2
                    list2[r1 - 2][r2] = 2
                    list2[r1 - 3][r2] = 2
                    list2[r1 - 4][r2] = 1
                    list2[r1 + 1][r2] = 1
                    list2[r1 + 1][r2 - 1] = 1
                    list2[r1][r2 - 1] = 1
                    list2[r1 - 1][r2 - 1] = 1
                    list2[r1 - 2][r2 - 1] = 1
                    list2[r1 - 3][r2 - 1] = 1
                    list2[r1 - 4][r2 - 1] = 1
                    list2[r1][r2 + 1] = 1
                    list2[r1 + 1][r2 + 1] = 1
                    list2[r1 - 1][r2 + 1] = 1
                    list2[r1 - 2][r2 + 1] = 1
                    list2[r1 - 3][r2 + 1] = 1
                    list2[r1 - 4][r2 + 1] = 1
                    w4 += 1
        elif r3 == 1: # right
            if r2 != 10 and r2 != 9 and r2 != 8:
                if list2[r1][r2] == 0 and list2[r1][r2 + 1] == 0 and list2[r1][r2 + 2] == 0 and list2[r1][r2 + 3] == 0:
                    list2[r1][r2] = 2
                    list2[r1 - 1][r2] = 1
                    list2[r1 + 1][r2] = 1
                    list2[r1][r2 + 1] = 2
                    list2[r1][r2 + 1] = 2
                    list2[r1 + 1][r2 + 1]
                    list2[r1 - 1][r2 - 1] = 1
                    list2[r1][r2 - 1] = 1
                    list2[r1 + 1][r2 - 1] = 1
                    list2[r1][r2 + 2] = 2
                    list2[r1 - 1][r2 + 2] = 1
                    list2[r1 + 1][r2 + 2] = 1
                    list2[r1][r2 + 3] = 2
                    list2[r1 - 1][r2 + 3] = 1
                    list2[r1 + 1][r2 + 3] = 1
                    list2[r1 - 1][r2 + 4] = 1
                    list2[r1][r2 + 4] = 1
                    list2[r1 + 1][r2 + 4] = 1
                    w4 += 1 
draw_ship1()
draw_ship2()
draw_ship3()
draw_ship4()
del list2[0]
del list2[10]
del list2[0][0]
del list2[1][0]
del list2[2][0]
del list2[3][0]
del list2[4][0]
del list2[5][0]
del list2[6][0]
del list2[7][0]
del list2[8][0]
del list2[9][0]
del list2[0][10]
del list2[1][10]
del list2[2][10]
del list2[3][10]
del list2[4][10]
del list2[5][10]
del list2[6][10]
del list2[7][10]
del list2[8][10]
del list2[9][10]
list_enemy = list2