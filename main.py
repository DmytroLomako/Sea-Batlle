from turtle import *
from modules.enemyships import list_enemy
from modules.click import click
from modules.map import draw_field, text
# from modules.button import button

tracer(0, 0)
speed(0)
hideturtle()
for i in list_enemy:
    print(i)
text()
onscreenclick(click)
draw_field(-350, 150)
draw_field(50, 150)
update()
mainloop()