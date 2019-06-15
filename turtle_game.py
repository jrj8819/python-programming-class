import turtle
t = turtle.Turtle()

score = 0 # 점수
time = 0 # 사용자의 입력횟수
TRIAL = 100 # 최대 100회 입력
GAP = 3

# 상자의 객체
box = [turtle.Turtle(), turtle.Turtle(), turtle.Turtle(),
      turtle.Turtle(), turtle.Turtle(), turtle.Turtle()]

# 상자의 위치 좌표
box_pos = [(150,50), (-250,100), (200,-250), (-200,-150), (150,300), (-100,200)]

# 상자를 생성 및 배치하는 함수
def createBox():
    for i, b in enumerate(box):
        b.up()
        b.goto(box_pos[i])
        b.shape("square")

# 거북이를 생성 및 배치하는 함수
def createTurtle():
    t.shape("turtle") # 거북이 모양 출력
    t.up() # 선 표시하지 않음
    t.goto(0,0) # 거북이 좌표 이동
    t.left(90)
    t.speed(1) # 거북이 속도
    t.pensize(5) # 선 굵기
    t.color("red") # 거북이, 선색

# 거북이와 상자의 충돌 여부를 감지하는 함수
""" return : 충돌하면 상자의 인덱스 번호, 안하면 -1"""
def checkCrash(box_pos, x, y):
    print("*" * 100)
    for i, (p_x, p_y) in enumerate(box_pos): # 박스 좌표 인덱스, 박스 X좌표, 박스 Y좌표    
        # 이미 충돌한 박스의 좌표는 -1, -1이므로 검사에서 제외
        if p_x == -1 and p_y == -1: 
            continue
        # 박스(p_x, p_y)와 거북이(x, y)의 좌표 비교
        # 두 좌표값의 절대값 차이가 3인 경우 충돌로 판정
        if ((abs(p_x)-abs(x) < GAP) and (abs(p_x)-abs(x) > (-1*GAP))):
            if ((abs(p_y)-abs(y) < GAP) and (abs(p_y)-abs(y) > (-1*GAP))):
                # 좌표의 부호가 서로 같을 경우에만 충돌로 판정
                """p_x : 150, x : -150, p_y : -250, x : 250
                인 경우는 충돌로 판정하지 않는다"""
                if (p_x < 0 and x < 0) or (p_x > 0 and x > 0):
                    if (p_y < 0 and y < 0) or (p_y > 0 and y > 0):
                        return i
        else:
            continue
    return -1

# 충돌한 박스 처리 함수
def removeBox(b, b_pos, idx):
    b[idx].color("red") # 충돌한 박스 색상 전환
    b_pos[idx] = (-1, -1) # 좌표 -1,-1로 변환11
    
# 점수 계산
def calcScore(x1, y1, x, y):
    return ((x1-x) ** 2 + (y1-y) ** 2) ** 0.5

# 거북이를 왼쪽으로 이동하는 함수
def leftTurtle():
    t.left(90)
    t.forward(50)

# 거북이를 오른쪽으로 이동하는 함수
def rightTutle():
    t.right(90)
    t.forward(50)

# 남은 기회 출력하는 함수
def printTry(max_times, try_count):
    print("남은 기회가 %d 회 남았습니다." % (max_times - try_count))
    return max_times - try_count

# 남은 점수 출력하는 함수
def printScore(s):
    print("현재 점수는 %d 점 입니다." % s)

# 게임 방법 출력하는 함수
def printHowto():
    print("거북이를 움직여 상자를 먹는 게임입니다.")
    print("움직일 수 있는 30번에 기회 안에 최대한 상자를 먹어 점수를 올리세요.")
    print("1을 입력을 하면 좌측으로, 2를 입력하면 우측으로 움직입니다.")
    print("종료하려면 'q'를 입력하세요.")

# 게임 메인 코드
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




