from turtle import *

left(90)
tracer(0)
screensize(3000, 3000)

k = 30
for i in range(2):
    forward(10*k)
    right(90)
    forward(18*k)
    right(90)

pu()

for i in range(5):
    forward(5*k)
    right(90)
    forward(7*k)
    left(90)

pd()

for i in range(2):
    forward(10*k)
    right(90)
    forward(7*k)
    right(90)

pu()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(5, "red")
        dot(2, "white")

update()

done()
