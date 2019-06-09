import turtle
t = turtle.Turtle()
scr = turtle.Screen()
scr.setup(1000,800)
score = 0
time = 0
box = [turtle.Turtle(), turtle.Turtle(), turtle.Turtle(),
      turtle.Turtle(), turtle.Turtle(), turtle.Turtle()]
box_pos = [(150,50), (-250,100), (200,-250), (-200,-150), (150,300), (-100,200)]

def createBox():
    for i, b in enumerate(box):
        b.up()
        b.goto(box_pos[i])
        b.shape("square")
    
def createTurtle():
    t.shape("turtle") # 거북이 모양 출력
    t.up() # 선 표시하지 않음
    t.goto(0,0) # 거북이 좌표 이동
    t.left(90)
    t.speed(1) # 거북이 속도
    t.pensize(5) # 선 굵기
    t.color("red") # 거북이, 선색

def checkCrash(box_pos, x, y):
    for i, (p_x, p_y) in enumerate(box_pos):
        if p_x == -1 and p_y == -1:
            print("terminated : %d %d %d %d" % (p_x, p_y, x, y))
            continue
        print("check : %d %d %d %d" % (p_x, p_y, x, y))
        if p_x == x and p_y == y:
            print("crashed : %d %d %d %d" % (p_x, p_y, x, y))
            return i
        else:
            continue
    print("returned : %d %d %d %d" % (p_x, p_y, x, y))              
    return -1

def removeBox(b, b_pos, idx):
    b[idx].color("red")
    b_pos[idx] = (-1, -1)
    

def calcScore(x1, y1, x, y):
    return ((x1-x) ** 2 + (y1-y) ** 2) ** 0.5

def leftTurtle():
    t.left(90)
    t.forward(50)

def rightTutle():
    t.right(90)
    t.forward(50)

def printTry(max_times, try_count):
    print("남은 기회가 %d 회 남았습니다." % (max_times - try_count))
    
    return max_times - try_count
    
def printScore(s):
    print("현재 점수는 %d 점 입니다." % s)

def printHowto():
    print("거북이를 움직여 상자를 먹는 게임입니다.")
    print("움직일 수 있는 30번에 기회 안에 최대한 상자를 먹어 점수를 올리세요.")
    print("1을 입력을 하면 좌측으로, 2를 입력하면 우측으로 움직입니다.")
    print("종료하려면 'q'를 입력하세요.")
    
createTurtle()
createBox()
printHowto()

while True:
    u_in = input()
    if u_in == "1":
        leftTurtle()
    elif u_in == "2":
        rightTutle()
    elif u_in == "q":
        break;
    
    check = checkCrash(box_pos, int(t.xcor()), int(t.ycor()))
    
    if check != -1:
        removeBox(box, box_pos, check)
        
        score += calcScore(int(t.xcor()), int(t.ycor()), 0, 0)
    
        printScore(score)
    if time == 300:
        break
    else:
        pass
        
    time += 1
    if printTry(300, time) == 0:
        print("게임 종료")
        printScore(score)
        break
