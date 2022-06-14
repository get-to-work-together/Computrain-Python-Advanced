import turtle

# instantie
t = turtle.Turtle()

# variable
distance = 100
n = 9
angle = 360 / n

# commands - methods
for _ in range(n):
    t.forward(distance)
    t.left(angle)

# klaar
turtle.done()









