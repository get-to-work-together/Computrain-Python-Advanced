# https://nl.wikipedia.org/wiki/Regelmatige_veelhoek

import turtle

t = turtle.Turtle()

t.color('red')

n = 5
# angle = 360/n   # 180 - (180 - 360/n)
angle =180 - (180 - 360/n)

for _ in range(n):
    t.fd(100)
    t.left(angle)

turtle.done()