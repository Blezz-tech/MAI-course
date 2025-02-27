from turtle import *

left(90)
tracer(0)
screensize(1000, 1000)

k = 20
right(315)
for i in range(7):
    forward(16*k)
    right(45)
    forward(8*k)
    right(135)

pu()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(5, "red")
        dot(2, "white")

update()

done()
