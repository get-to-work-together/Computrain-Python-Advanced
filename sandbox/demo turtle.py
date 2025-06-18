
import turtle as t

t.speed(20)

n = 9
angle = 360 / n
distance = 500 / n

t.fillcolor('orange')
t.begin_fill()

for i in range(n):
    t.forward(distance)
    t.left(angle)

t.end_fill()

t.done()