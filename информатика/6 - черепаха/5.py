from turtle import *

left(90)
tracer(0)
screensize(10000, 10000)

k = 100
for i in range(4):
    forward(12*k)
    right(90)

for i in range(3):
    forward(12*k)
    right(120)

pu()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(5, "red")
        dot(2, "white")

update()

done()
