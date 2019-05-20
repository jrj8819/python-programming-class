# 키보드의 입력을 받는 명령어 input() (재정리)

"""
키보드의 입력을 받을 수 있는 input() 함수
(함수 = 특정 기능을 하기 위한 명령어의 집합)
결과(리턴) : 입력 받은 내용을 메모리에 저장

메모리에 있는 값을 변수에 저장하여 활용하자!

변수 = input()

변수 안에 있는 데이터는 문자열이다.

데이터를 숫자로 바꾸려면 문자를 숫자로 바꾸는
형변환 과정을 거쳐야 한다.

변수 = int(input())

1(문자) >> 1(숫자)
korea(문자) >> ??(숫자)

문자열을 숫자로 형변환 >> int(변수 혹은 값)
숫자를 문자열로 형변환 >> str(변수 혹은 값)
"""
"""
user_input = input()
print(user_input)
user_input = int(user_input)

user_input = str(user_input) 
print(type(user_input))
"""
# Quiz) 키보드로 입력을 3번 받아 리스트에 저장
# 하고 출력하세요.
"""
num1 = input()
num2 = input()
num3 = input()

myList = [num1, num2, num3]
print(myList)
"""

# 리스트의 요소 삭제하기
"""
리스트 안의 값을 인덱스 혹은 슬라이스로
지정하여 삭제할 수 있다.

1. 인덱스로 지우기
del 리스트 이름[인덱스 번호]

2. 슬라이스로 지우기
del 리스트이름[슬라이스 처음 : 슬라이스 마지막]
혹은
리스트 이름[슬라이스 처음 : 슬라이스 마지막] = []
"""

myList = ['빨강', '노랑', '주황', '초록']
myList[1:3] = []
print(myList)

# Quiz 다음과 같이 리스트가 있을 때 요소를 삭제하세요
# ['a', 'b', 1, 4, 'f', '빨강']
# >> 1, 4, 빨강

# ['한국', '중국', ['태국', '필리핀','방콕']]  
# >> 필리핀,방콕

list1 = ['a', 'b', 1, 4, 'f', '빨강']
del list1[2:4]
del list1[-1]
# del list1[2:4], list1[-1]
print(list1)


list2 = ['한국', '중국', ['태국', '필리핀','방콕']]
del list2[2][1:]
print(list2)



# 리스트의 요소 추가하는 append()
"""
리스트의 요소를 추가한다.
리스트변수.append('추가할 요소값')

요소를 추가하면 인덱스가 늘어나고 가장 우측에 요소가
추가된다.
"""

myList = ['red','blue']
myList.append('yellow')
myList.append(['pink', 'green'])
print(myList)

# 리스트의 요소를 정렬하는 sort()
"""
리스트 안의 요소를 오름차순(뒤로 갈수록 숫자가 증가)으로
정렬된다.
리스트변수.sort()

문자는 사전(알파벳)숫서대로 정렬된다.
오름차순(뒤로 갈수록 문자가 순서 증가)
"""
myList = [1,2,10,4,5]
myList.sort()
print(myList)

myList2 = ['apple', 'a', 'b', 'c', 'bear']
myList2.sort()
print(myList2)

# 리스트의 순서를 바꾸는 reverse()
"""
리스트의 앞과 뒤의 인덱스 순서를 바꾼다.
리스트변수.reverse()
"""
myList3 = [1,2,10,4,5]
myList3.reverse()
print(myList3)

# Quiz) 다음 리스트를 내림 차순 정렬하세요

# myList = [1,2,10,4,5]

# myList2 = ['apple', 'a', 'b', 'c', 'bear']
print("="*40)
myList = [1,2,10,4,5]
myList.sort()
myList.reverse()
print(myList)

myList2 = ['apple', 'a', 'b', 'c', 'bear']
myList2.sort()
myList2.reverse()
print(myList2)

# 요소의 인덱스 찾기
"""
index() 함수로 리스트 안 요소의 인덱스 번호를 알수 있다.
리스트이름.index(찾고싶은 요소 값)
찾고 싶은 요소 값이 리스트에 없으면 에러가 발생된다.
"""
myList2 = ['apple', 'a', 'b', 'c', 'bear']
print(myList2.index('b'))

# 특정 인덱스를 지정하여 값 추가하기
"""
항상 리스트의 마지막에 값을 넣는 append()와는 달리
특정 위치(인덱스)를 선택하여 요소를 추가하는 insert()

insert(요소를 넣고 싶은 인덱스, 추가할 요소 값)
"""
myList2 = ['apple', 'a', 'b', 'c', 'bear']
myList2.insert(2, "hello")

print(myList2)

# 리스트 안에 값을 찾아서 지우는 remove()
"""
리스트변수.remove(삭제할 값)
삭제할 값이 리스트 안에 여러개 일 경우는
인덱스 번호가 빠른(가장 앞에 있는)값을 지운다.

"""

myList2 = ['apple', 'a', 'b', 'b', 'c', 'bear']
myList2.remove('b')
print(myList2)


# 리스트의 마지막 요소를 꺼내고 출력(리턴)하는 pop()
"""
리스트에서 마지막 요소(인덱스번호가 가장 큰)를 리스트에서
지우고 그 값을 변수에 저장할 수 있는(출력,리턴) 함수

지우는 값을 저장하는 변수 = 리스트변수.pop()
"""
myList2 = ['apple', 'a', 'b', 'b', 'c', 'bear']
a = myList2.pop()
print(myList2)
print(a)


# 리스트에서 값 지우기
"""
del >> 인덱스, 슬라이드로 지운다. 지운 값은 따로 저장 안됨.
remove >> 값으로 지운다. 지운 값은 따로 저장 안됨.
pop >> 마지막 요소 만 지운다. 지운 값을 따로 저장할 수 있다.
"""

# 리스트의 특정 값 개수 세기 count()
"""
리스트 안에 있는 특정 값의 개수를 센다.
리스트변수.count(찾을 값)

참고) 리스트 안의 요소의 갯수 len()
"""
myList2 = ['apple', 'a', 'b', 'b', 'c', 'bear']
print(myList2.count('b'))
print(len(myList2))


# 리스트의 확장
"""
extend() 함수는 리스트의 요소를 늘려준다
(리스트에 리스트를 붙인다.)

리스트이름.extend(리스트)
리스트이름 = 리스트이름 + 붙이는리스트
"""
myList2 = ['apple', 'a', 'b', 'b', 'c', 'bear']
myList2.extend(["web", "program"])
print(myList2)


# 튜플 (tuple)
"""
수정/삭제하지 못하는 리스트
튜플을 만들때는 소괄호()를 사용한다.

튜플을 저장하는 변수 = (요소, 요소, 요소)
튜플을 저장하는 변수 = ()
튜플을 저장하는 변수 = (요소,) >> 튜플의 요소가 1개
튜플을 저장하는 변수 = (요소, (요소, 요소)) >> 중첩
튜플을 저장하는 변수 = 요소, 요소 >> 소괄호 생략(비추)
"""

t = ('red', 'green', 'blue')
# t[1] = 'yellow'
# del t[1]
print(t[1:])


# 튜플 합치기(+)와 여러번 합치기(*)
"""
튜플의 데이터는 수정할 수 없지만
튜플 자체는 합치거나 여러번 합칠 수 있다.
"""

t = ('red', 'green', 'blue')
t2 = ('pink',)
t = t + t2
print(t)

print(t*3)

# 튜플과 리스트 간의 자료 형변환
"""
튜플의 요소 값은 수정 할 수 없으므로
리스트로 변환하면 요소 값을 수정할 수 있다.

리스트를 튜플로 형변환 >> 변수이름 = tuple(리스트)
튜플을 리스트로 형변환 >> 변수이름 = list(튜플)
"""
# 리스트를 튜플로 형변환 > 튜플을 리스트로 형변환
l = ['a','b','c']
print(type(l))

t = tuple(l)
print(type(t))

t = ('a','b','c]')
print(type(t))
# 튜플을 리스트로 형변환 > 리스트를 튜플로 형변환 
l = list(t)
print(type(l))
l[2]='c'
print(l)

t = tuple(l)
print(type(t))


# 딕셔너리
"""
데이터를 키(key)와 값(value)의 쌍으로 저장한
자료형태(자료구조)

변수 = {키1 : 값1, 키2 : 값2, 키3 : 값3 ...}

딕셔너리안에 값을 가져오려면
변수[키1] >> 형태로 값1을 가져올 수 있다.

키는 문자열, 숫자
값은 문자열, 숫자, True/False(참/거짓),리스트, 튜플,
    딕셔너리, 집합

자료형으로 지정할 수 있다.

"""

dic = {"name" : "pey", 1:"0119993323", 2 : "hello"}
dic[1] = "파이썬"
print(dic)



























































































































