from turtle import *

left(90)
tracer(0)
screensize(10000, 10000)

k = 40
for i in range(3):
    forward(7*k)
    right(90)

forward(10*k)

for i in range(3):
    left(90)
    forward(6*k)

pu()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(5, "red")
        dot(2, "white")

update()

done()
