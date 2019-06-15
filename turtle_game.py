import turtle
t = turtle.Turtle()

score = 0
time = 0
TRIAL = 100
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
    print("*" * 100)
    for i, (p_x, p_y) in enumerate(box_pos):
        print("[check] %d %d %d %d\n" % (p_x, p_y, x, y))
        
        if p_x == -1 and p_y == -1:
            print("[terminate] %d %d %d %d\n" % (p_x, p_y, x, y))
            continue
        
        if ((abs(p_x)-abs(x) < 3) and (abs(p_x)-abs(x) > -3)):
            print("check X")
            if ((abs(p_y)-abs(y) < 3) and (abs(p_y)-abs(y) > -3)):
                print("check Y")
                if (p_x < 0 and x < 0) or (p_x > 0 and x > 0):
                    print("check X_abs")
                    if (p_y < 0 and y < 0) or (p_y > 0 and y > 0):
                        print("check Y_abs")
                        print("[crash] %d %d %d %d\n" % (p_x, p_y, x, y))
                        return i
        else:
            print("[pass] %d %d %d %d\n" % (p_x, p_y, x, y))
            continue
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
    
    check = checkCrash(box_pos, t.xcor(), t.ycor())
    
    if check != -1:
        removeBox(box, box_pos, check)
        
        score += calcScore(t.xcor(), t.ycor(), 0, 0)
        
        printScore(score)
    if time == TRIAL:
        break
    else:
        pass
        
    time += 1
    if printTry(TRIAL, time) == 0:
        print("게임 종료")
        printScore(score)
        break




