# 모듈
"""
만들어 놓은 클래스, 함수, 변수를 별도의 파일로 만들어
필요할 때 불러와 쓸 수 있도록 하는 방법

import 모듈이름(파일이름)

모듈이름.함수()
모듈이름.변수
모듈이름.객체이름()
"""
"""
import Calculator
result = Calculator.mySum(1,2)
print(result)

print(Calculator.pi)

import Person
p = Person.Person('남')
p.printGender()

"""
# 또다른 표현방법
"""
import 모듈이름 as 별명
from 모듈이름 import [함수이름, 객체이름, 변수이름]
 >> 특정 함수, 객체, 변수 만 가져오므로
 참조할때 모듈이름이 필요없다.

from 모듈이름 import *
import Calculator as cal
from Calculator import mySum, myMulti

#print(Calculator.pi)
result = myMulti(1,2)
print(result)
#result = cal.myMulti(1,2)
#print(result)
#import Circle
from Circle import *
print('*'*50)
c = Circle((0,0), 10)
print(c.calArea())
"""

# 모듈로 불러올 때 실행하고 싶지 않은 부분 설정
"""
if __name__ == "__main__":
    실행하고 싶지 않은 부분

__name__ : 파이썬 모듈의 이름을 저장하는 내부 변수
__main__ : 실행한 파이썬 파일일 경우 저장되는 값
            모듈로 읽어오면 모듈이름이 __name__에 저장
"""

# 패키지
"""
모듈을 같은 용도에 따라 분류해 놓은 모듈의 모음
패키지는 파일을 같은 폴더에 넣어 만든다

import 폴더이름.모듈이름
from 폴더이름.모듈이름 import 함수, 변수, 클래스(객체)
"""

import my.Circle
c = my.Circle.Circle((0,0), 10)
print(c.calArea())

from my.Circle import *
c = Circle((0,0), 15)
print(c.calArea())


# 예외처리
"""
프로그램이 동작하면서(사용자가 사용하면서) 발생하는
런타임 에러에 대해 대비하기 위한 방법

try:
    에러가 날수도 있는 부분
except 오류이름 as 오류메시지변수:
    오류에 대처하는 코드

발생오류종류

ZeroDivisionError : 0으로 나눈 경우
NameError : 변수명이 없는 경우
IndexError : 문자열, 리스트에서 인덱스 잘못 입력한 경우

오류 종류 확인 사이트
https://docs.python.org/ko/3/library/exceptions.html
"""
"""
num = int(input())
"""
"""
try:
    print(100/num)
    print(num2)
except ZeroDivisionError as e:
    print("에러가 발생하였습니다 : %s." % e)
except NameError as e:
    print("에러가 발생하였습니다 : %s." % e)
"""
"""
except 부분은 에러 종류에 따라 여러개 쓸 수 있다.

에러 종류가 불분명 할때는 Exception 키워드를 오류이름
대신에 쓴다.
"""
"""
try:
    print(100/num)
    print(num2)
except Exception as e:
    print("알지 못하는 에러가 발생했습니다. : %s" % e)

    if e == "division by zero":
        print("0으로 나눌수 없습니다.")
"""

"""
try:
    에러가 날수도 있는 부분
except 오류이름 as 오류메시지변수:
    오류에 대처하는 코드
else:
    오류가 발생하지 않았 때
finally:
    오류가 발생/발생하지 않았을 때 모두 실행되는 부분 
"""
"""
try:
    f = open('c:\song123.txt', 'r')
except FileNotFoundError as e:
    print("에러가 발생하였습니다. : %s" % e)
else:
    print(f.read())
finally:
    f.close()
"""
# Quiz
# myDiv()함수에 0으로 나누었을 때 발생하는
# 예외 처리를 적용해 봅시다.

# TypeError : 연산을 위한 자료형이 다를경우
# 발생하는 에러


# 오류 발생시키는 키워드 raise
"""
raise 오류이름

해당 오류를 발생시키는 동작을 한다.

1) 예외 처리 부분을 테스트하기 위해서
특정 오류를 발생시킬 때 활용한다.

2) 사용자가 정의한 에러를 실행시킬 때
활용한다.
"""
"""
def myDiv2(a,b):
    try:
        # 숫자를 직접 나누는 대신에
        # 실행 흐름이 except ZeroDivisionError 부분으로 이동
        raise ZeroDivisionError
        # 아래 result 부분은 실행 되지 않음
        result = a/b
    except ZeroDivisionError as e:
        # 예외 처리 부분을 실행하여 테스트
        print("0으로 나눌수 없음 : %s" % e)
        return None
    except TypeError as e:
        print("연산이 불가능함 : %s" % e)
        return None
    else:
        return result

"""
# 사용자 정의 예외
"""
사용자가 프로그램의 용도 / 특징에 맞게 정의한 예외

Exception 클래스를 상속받아 만든다.
"""

class MyException(Exception):
    msg = "입력 내용이 잘못 되었습니다."

    def __str__(self):
        return self.msg
"""
u_input = input()
if u_input == "":
    raise MyException
else:
    print(u_input)
"""
"""
u_input = input()
try:
    if u_input == "":
        raise MyException
    else:
        print(u_input)
except MyException as e:
    print(e)
"""
# 자주쓰는 내장 함수

print(abs(-1.2))

print(all([1,2,3,0]))

print(any([0,0,0,0]))

print(chr(65))

print(dir(c))

print(divmod(10,5))

# 1) enumerate
"""
for문에서 리스트를 활용할 때
인덱스와 값을 같이 for문 내에서 쓸 수 있다.
"""
idx = 0
for i in ['a','b','c']:
    print(idx)
    print(i)
    idx += 1

for idx, val in enumerate(['a','b','c']):
    print(idx)
    print(val)
    print("@@@@@")


print(eval('1+2'))

def f(x):
    return x > 0

print(list(filter(f, [1, -2, -3, 2])))


print(hex(777))


# 2) 객체의 주소를 알려주는 id
num = 1
num2 = 2

print(id(num))
print(id(num2))


# 3) 형변환 int(), float(), list(), tuple(), dict(), set(), str()

# 4) 객체가 만들어진 클래스를 비교 하는 isinstance

class People:
    pass
class People2:
    pass
a = People()

print(isinstance(a, People2))

# 5) 간단한 함수를 만들 수 있는 lambda

year = ['1980', '1990', '2000', '2010', '2020']   

def addS(year):
    result = []
    for i in year:
        result.append(i + 's')

    return result

print(addS(year))

myLambda = lambda year : year + 's'

print(myLambda('1990'))

# 6) 데이터와 계산하는 함수를 연결해주는 map

print(list(map(myLambda, year)))
print(list(map(lambda year : year + 's', year)))

print(list(filter(lambda year : year == '1990',
                  year)))


# Quiz
# 람다 함수를 활용하여, 다음 리스트의 값을 제곱하여 리스트로 만들어 출력하세요.
mylist = [4,5,3,7,54,3,6,8,9,6,4,3,2,2,1,4,65,7,4,3,2]


mylamb = lambda x : x * x
print(mylamb(2))

result = list(map(mylamb, mylist))
print(result)


print(max(result))

print(min(result))

print(oct(777))

print(ord('A'))

print(chr(65))

print(5 ** 2)
print(pow(5,2))

# 범위를 지정하는 range
"""
range(첫번호, 끝번호, 간격)
"""
print(list(range(0, 10, 2))) # 0,2,4,6,8

# 리스트 안에 내용을 정렬하는 sorted
mylist = [4,5,3,7,54,3,6,8,9,6,4,3,2,2,1,4,65,7,4,3,2]

print(sorted(mylist))

# 다수의 리스트를 튜플로 묶을 때 활용하는 zip

nation = ['한국', '중국', '일본']
eng_nation = ['korea','china','japan']

for i in range(3):
    print('%s %s' % (nation[i], eng_nation[i]))

for k, e in zip(nation, eng_nation):
    print('%s %s' % (k, e))


# time 모듈
import time
print(time.time())

today = time.localtime(time.time())
print(today)
print(today[0])

print(today[1])

print(today[2])


# time.sleep(10)
"""
for i in range(100):
    print(i+1)
    time.sleep(1)
"""








