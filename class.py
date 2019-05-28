# Quiz)
# 애국가.txt 파일을 읽어 같은 내용의 '애국가 복사본.txt 파일을
# 만드세요

f = open("c:\애국가.txt", "r")
read_file = f.read()
f.close()

f = open("c:\애국가 복사본.txt", "w")
f.write(read_file)
f.close()

# with와 open()
with open("c:\애국가.txt", "r") as f:
    read_file = f.read()
    print(read_file)

"""
with 키워드와 Open()를 같이 쓰면 with 키워드의
실행 블록(들여쓰는 부분)이 다 실행 되면
자동으로 close() 함수를 호출하여
편리하다.
"""

with open("c:\애국가.txt", "r") as f:
    read_file = f.read()

with open("c:\애국가 복사본.txt", "w") as f:
    f.write(read_file)



# 객체 지향과 절차 지향 프로그래밍
"""
절차지향 : 코드를 순서대로(위 아래) 작성하여 로직을 구성하는 프로그래밍 방법,
프로젝트가 커질수록 참여 인원이 많아질 수록 관리가 어렵다.

객체 : 사물, 사람, 동물 등 세상에 있는 대상
객체지향 : 사물, 사람 등 대상을 프로그래밍으로 모델링하는 프로그래밍 방법
대상에 대해 데이터(키, 무게 등)와 행동(노래를 부른다, 걸어 다닌다)으로 나누어 사물을 모델링

강아지

데이터 : 강아지의 나이, 색상, 견종
행동(기능) : 사료를 먹는다, 짖는다.

데이터 >> 변수
행동(기능) >> 함수

클래스 : 사물의 데이터와 행동을 변수와 함수로 지정하여 만들어 놓은 구조
"""

# Quiz) 보조베터리, 에어콘, 택배보관함 를 대상으로 데이터와 행동 5개씩 선정하기
"""
보조베터리
데이터 : 충전량, 단자 수, 모델명
행동(기능) : 충전하기, 잔량확인하기, 과충전방지하기

에어콘
데이터 : 적정 평수, 설치 타입, 색상
행동(기능) : 냉방하기, 먼지거르기, 온도출력하기

택배보관함
데이터 : 비밀번호, 보관함 가격, 보관함 위치
행동(기능) : 택배찾기, 문자알림, 도난알림
"""

# 클래스 만드는 문법
"""
class 클래스이름:
    변수1
    변수2
    
    def 함수이름(self,매개변수):
        함수 실행 부분

    def 함수이름2(self,매개변수):
        함수 실행 부분
"""

class Dog:
    age = 1
    color = "gold"
    dog_type = "골든 리트리버"

    def eat(self):
        print("강아지가 밥을 먹습니다")

    def bark(self):
        print("강아지가 멍멍 합니다")
        

# 클래스로 부터 객체 만드는 명령
"""
객체를 저장할 변수 = 클래스이름()
"""
dog = Dog()

# 클래스의 변수 읽어오기, 함수 실행하기
"""
객체 변수.(클래스)변수
객체 변수.함수()
"""
dog.age = 2

class buyer:
    money = 10000
    apple = 0
    price = 0
    
    def buy(self, ea, price):
        print("%d 개의 사과를 삽니다." % ea)
        if self.money >= (ea * price):           
            self.apple = self.apple + ea
            self.money = self.money - (ea * self.price)
        else:
            print("구매할 수 없습니다.")
            
    def askPrice(self):
        print("사과 얼마에요?")
        
class seller:
    money = 10000
    apple = 100
    price = 10

    def answerPrice(self):
        print("%d원 입니다" % self.price)

    def sell(self, ea, price):
        if self.apple >= ea:
            self.apple = self.apple - ea
            self.money = self.money + (ea * self.price)
        else:
            print("판매할 수 없습니다.")
                  
buyer = buyer()
seller = seller()

buyer.askPrice()
seller.answerPrice()
buyer.buy(2, 10)
seller.sell(20000, 10)


# 객체지향 프로그래밍은?
"""
객체간에 데이터를 주고 받는 형태로
전체적인 처리 로직을 프로그래밍하는 방법
"""

# self
"""
클래스를 만드는 중에 self는 클래스 안에 있는
변수(클래스 변수)를 가져올 때 활용하고,
클래스 안에 있는 함수(클래스 함수)에 첫번째 매개변수로
포함됩니다.(생략불가)
"""



# init 함수
"""
객체 생성과 동시에 클래스의 변수를 초기화 하고 싶은 경우에
활용한다.

def __init__(self, 초기값1, 초기값2 ...):
    클래스의변수1 = 초기값1
    클래스의변수2 = 초기값2

"""

# 클래스 변수와 인스턴스 변수
"""
클래스에서 쓸수 있는 변수의 종류 2가지
클래스 변수 : 클래스로 만든 모든 객체들이 공유하는
             변수
인스턴스 변수 : 객체마다 가지고 있는 변수

두 변수 모두 만드는 방법은 동일하다.

"""

class Employee:
    number = 0
    company = ""
    
    def __init__(self, name, company):
        self.name = name
        Employee.number += 1
        Employee.company = company
        
    def fire(self):
        Employee.number -= 1

    def newName(self, newName):
        Employee.company = newName

p1 = Employee("kim", "무한상사")
p2 = Employee("Lee", "무한상사")

print(p1.company)
print(p2.company)


p1.newName("더조은")

print(p1.company)
print(p2.company)

# 상속
"""
클래스들의 공통적인 함수, 변수 등을 그대로 가져와서
새로운 클래스를 작성할 수 있는 방법

부모 클래스 : 공통적인 함수&변수를 가지고 있는 클래스
자식 클래스 : 부모 클래스로 부터 만들어진 새로운 클래스

자식 클래스를 만들려면
class 클래스이름(부모클래스의 이름):
    클래스의 내용
"""
"""
class Person:
    def __init__(self, gender):
        self.gender = gender

    def printGender(self):
        print(self.gender)

class Fireman(Person):
    def __init__(self, gender):
        self.gender = gender
        
    def clearFire(self):
        print("불을 끕니다")

fireman = Fireman("남성")
fireman.printGender()

class Car:
    color = "sliver"
    def turnOn(self):
        print("시동을 겁니다")


class Truck(Car):
    color = "red"
    def turnOn(self):
        print("부르르릉 시동을 겁니다")
        
    def carryOn(self):
        print("짐을 실었습니다.")

t = Truck()
t.turnOn()
"""
"""
부모 클래스에 저장되어 있는 변수값을
자식 클래스에서도 활용할 수 있다.
단, 부모클래스에서 __init__()함수의 매개변수로 변수값을 받으면,
자식 클래스에서도 __init__()함수의 매개변수로 변수값을 받아야한다.
"""
# 재정의(오버라이딩, overiding)
"""
자식 클래스는 부모 클래스의 변수 함수와 같은
이름의 변수 함수를 새로 만들수 있다
"""

# 연산자 오버로딩(overloading)
"""
연산자에 기본 기능외에 다른 기능을 추가하여 만드는 방식
클래스의 객체간에 연산자의 실행 방식을 정의할 수 있다.
각 연산자 마다 실행 방식을 정의할 수 있는 함수가 정해져 있다.
__add__ : +
__sub__ : -
__mul__ : *
__truediv__ : /
__mod__: %
"""

class People:
    name = ""
    def __init__(self, name): 
        self.name = name
        
    def __add__(self, other): 
        print("%s %s 친구가 되었습니다." %(self.name, other.name))

    def __sub__(self, other):
        print("%s %s 남남이 되었습니다." %(self.name, other.name))

    def __mul__(self, other):
        pass
    def __truediv__(self, other):
        pass
    
p1 = People("철수")
p2 = People("영희")

p1 + p2
p1 - p2 
p1 * p2
p1 / p2


# 모듈
"""
만들어 놓은 클래스, 함수, 변수를 별도의 파일로 만들어
필요할 때 불러와 쓸 수 있도록 하는 방법

import 모듈(파일)이름

변수 = 모듈이름.클래스명
모듈이름.함수명(매개변수)
모듈이름.변수명

or

from 모듈(파일)이름 import *

변수 = 클래스명
함수명(매개변수)
변수명
"""

#import Car

"""
car = Car.Car()
fun = Car.printCar()
print(Car.myCar)
"""
"""
from Car import *
car = Car()
#fun = printCar()
#print(myCar)
"""

"""
모듈을 읽어왔을 때 다른 파일에 있는 명령어가
실행되지 않도록 하려면
다음 조건을 적용한다.

if __name__ == "__main__":
    명령어

__name__ : 모듈의 이름을 저장하고 있는 변수, 불러와지는
            모듈은 자신의 파일 이름이 저장된다.
__main__ : 코드를 파이썬에서 직접 실행한 파일이면
            __name__변수에 들어가는 값
"""

# 패키지
"""
모듈을 같은 용도에 따라 분류해 놓은
모듈의 모음

패키지는 파일을 같은 폴더에 넣어 만든다
"""
from my.Car import *
car = Car()
fun = printCar()
print(myCar)

# 예외처리
"""
프로그램이 동작하면서(사용자가 사용하면서) 발생하는
에러에 대해 대비하기 위한 방법

try:
    실행하는 코드
except 발생오류이름 as 오류메시지저장변수 :
    오류에 대처하는 코드

발생오류종류
ZeroDivisionError : 0으로 나눈 경우
NameError : 변수명이 없는 경우
IndexError : 문자열, 리스트에서 인덱스 잘못 입력한 경

모든오류 종류 확인하는 링크
https://docs.python.org/ko/3/library/exceptions.html
"""
try:
    num = int(input())
    print(100/num)
except ZeroDivisionError as e:
    print("%s 에러가 발생했어요 " % e)






































































