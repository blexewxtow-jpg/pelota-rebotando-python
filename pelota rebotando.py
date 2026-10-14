import turtle
t =turtle.Turtle()
x=0
y=0
vx=5
vy=5
t.goto(x,y)
t.shape("circle")
t.color("orange")
t.penup()
while True:
    x = x + vx
    y = y + vy

    if x > 300:
        vx*=-1
    elif x < -300:
        vx*=-1

    if y > 280:
        vy*=-1
    elif y < -280:
        vy*=-1

    t.goto(x, y)


turtle.done()
