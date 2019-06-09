import turtle
t = turtle.Turtle()
scr = turtle.Screen()
t.shape("turtle")
t.goto(0,0)
t.color("black")

def redTurtle():
    t.color("red")

def blueTurtle():
    t.color("blue")

scr.onkeypress(redTurtle, '1')
scr.onkeypress(blueTurtle, 'Down')

scr.listen()
