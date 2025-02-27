from turtle import *

left(90)
tracer(0)
screensize(1000, 1000)

k = 20
for i in range(4):
    forward(6*k)
    right(90)
    forward(6*k)
    left(90)
    forward(6*k)
    right(90)

pu()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(5, "red")
        dot(2, "white")

update()

done()
