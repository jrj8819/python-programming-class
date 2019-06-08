import turtle
t = turtle.Turtle()

def createTurtle():
    t.shape("turtle") # 거북이 모양 출력
    t.up() # 선 표시하지 않음
    t.goto(0,0) # 거북이 좌표 이동
    t.speed(1) # 거북이 속도
    t.pensize(5) # 선 굵기
    t.color("red") # 거북이, 선색


def leftTurtle():
    t.left(90)
    t.forward(200)

def rightTutle():
    t.right(90)
    t.forward(200)

createTurtle()

time = 0
while True:
    u_in = input()
    if u_in == "1":
        leftTurtle()
    else:
        rightTutle()

    if time == 10:
        break
    time += 1
    print(time)
