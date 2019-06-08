# 거북이 모듈 임포트 및 객체 생성
import turtle
t = turtle.Turtle()

t.shape("turtle") # 거북이 모양 출력
t.up() # 선 표시하지 않음
t.goto(0,0) # 거북이 좌표 이동
t.speed(1) # 거북이 속도
t.pensize(5) # 선 굵기
t.color("red") # 거북이, 선색
t.goto(100,100)
"""
t.down() # 선 표시함
t.forward(100) # 머리방향으로 100만큼 이동
t.left(90) # 왼쪽으로 90도 전환
t.forward(100)
t.right(90) # 오른쪽으로 90도 전환
t.forward(100)
t.left(90)
t.forward(100)
"""
