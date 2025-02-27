from turtle import *

left(90)
tracer(0)
screensize(10000, 10000)

k = 50
for i in range(4):
    forward(10*k)
    right(270)

pu()

forward(3*k)
right(270)
forward(5*k)
right(90)

pd()

for i in range(2):
    forward(10*k)
    right(270)
    forward(12*k)
    right(270)

pu()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(5, "red")
        dot(2, "white")

update()

done()
