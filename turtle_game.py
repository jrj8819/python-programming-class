import turtle
scr = turtle.Screen()
scr.setup(1000,1000)
t = turtle.Turtle()
# 상자 객체들의 리스트
box = [turtle.Turtle(), turtle.Turtle(), turtle.Turtle(),
      turtle.Turtle(), turtle.Turtle(), turtle.Turtle()]
# 상자 좌표
box_pos = [(150,50), (-250,100), (200,-250),
           (-200,-150), (150,300), (-100,200)]
# 입력 횟수
time = 0

# 최대 입력 횟수
max_time = 355550

# 점수
score = 0

def createBox():
    for i, b in enumerate(box):
        b.up()
        b.goto(box_pos[i])
        b.shape("square")
        b.color("black")
"""
1입력하면 거북이가 왼쪽으로
2입력하면 거북이가 오른쪽으로 움직이도록
만드세요.
"""
def createTurtle():
    t.shape("turtle")
    t.up()
    t.goto(0,0)
    t.color("red")

def leftTurtle():
    t.left(90)
    t.forward(50)

def rightTurtle():
    t.right(90)
    t.forward(50)

def printTry(max_times, try_count):
    print("남은 기회가 %d 회 남았습니다."
          % (max_times - try_count))
    return max_times - try_count

def printHowto():
    print("거북이를 움직여 상자를 먹는 게임입니다.")
    print("움직일 수 있는 30번에 기회 안에 최대한 상자를 먹어 점수를 올리세요.")
    print("1을 입력을 하면 좌측으로, 2를 입력하면 우측으로 움직입니다.")
    print("종료하려면 'q'를 입력하세요.")

def calcScore(x1, y1, x, y):
    return ((x1-x) ** 2 + (y1-y) ** 2) ** 0.5

# 거북이와 상자의 충돌 여부를 판정하는 함수
"""
box_pos : 상자의 좌표
x, y : 거북이의 좌표
"""
def checkCrash(box_pos, x, y):
    for i, (bx, by) in enumerate(box_pos):
        # 이미 충돌한 박스는 인식하지 않는다
        if bx == -1 and by == -1:
            continue
        # 박스와 거북이의 위치가 같으면 충돌로 인식한다.
        if bx == x and by == y:
            return i
        else:
            continue
    return -1
        
def removeBox(idx, box_pos, box):
    box[idx].color("red")
    box_pos[idx] = (-1, -1)

def printScore(s):
    print("현재 점수는 %d 점 입니다." % s)
    
createTurtle()
createBox()
rightTurtle()

while True:
    u_in = input()

    if u_in == "1":
        leftTurtle()
    elif u_in == "2":
        rightTurtle()
    elif u_in == "q":
        break

    # 키를 입력하면 시도 횟수를 1증가한다.
    time += 1

    # 남은 횟수를 검사하여 출력하고
    # 0이면 게임을 종료한다.
    if printTry(max_time, time) == 0:
        print("게임 종료")
        printScore(score)
        break

    check = checkCrash(box_pos, t.xcor(), t.ycor())

    # 충돌 한 경우
    if check != -1:
        # 충돌한 박스는 지운다.
        removeBox(check, box_pos, box)

        # 점수를 계산하는 함수
        score += calcScore(t.xcor(), t.ycor(), 0, 0)

        printScore(score)


































