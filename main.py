from turtle import *
from modules.click import click
from modules.map import draw_field, text

tracer(0, 0)
speed(0)
hideturtle()
text()
onscreenclick(click)
draw_field(-350, 150)
draw_field(50, 150)
update()
mainloop()