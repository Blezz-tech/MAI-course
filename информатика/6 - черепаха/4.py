from turtle import *

left(90)
tracer(0)
screensize(1000, 1000)

k = 40
for i in range(4):
    forward(10*k)
    right(90)

right(30)

for i in range(5):
    forward(6*k)
    right(60)
    forward(6)
    right(120)

pu()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(5, "red")
        dot(2, "white")

update()

done()
