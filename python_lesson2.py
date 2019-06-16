# 리스트 연산자
"""
문자열과 같이 두 리스트를 하나로 합치고(+),
리스트를 여러번 이어 붙이는(*) 연산자이다.
"""

a = ["한국", "미국"]
b = ["일본", "중국"]

print(a + b)
print(a * 2)

# 리스트의 수정 / 삭제

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
#del myList[1:3]
#myList[1:3] = []
print(myList)


myList[0] = "RED"
print(myList)

myList[1:3] = ["YELLOW", "ORANGE"]
print(myList)


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

# 리스트의 순서를 바꾸는 reverse()
"""
리스트의 앞과 뒤의 인덱스 순서를 바꾼다.
리스트변수.reverse()
"""
print("="*40)
myList = [1,2,10,4,5]
myList.sort()
myList.reverse()
print(myList)

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
"""
num1 = input()
print(num1)
sp = num1.split(" ")
print(sp)

"""

# case 1)
"""
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

math_list = []

math_list.append(num1)
math_list.append(num2)
math_list.append(num3)
math_list.append(num4)
math_list.append(num5)

print(math_list)

avg = (math_list[0] + math_list[1] + math_list[2] + math_list[3] +  math_list[4]) /5
print("평균은 %d 점입니다" % avg)
"""
"""
# case 2)
math_list = [int(input()),
             int(input()),
             int(input()),
             int(input()),
             int(input())]

avg = (math_list[0] + math_list[1] +
       math_list[2] + math_list[3] +
       math_list[4]) / len(math_list)

print("평균은 %d 점입니다" % avg)
"""
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
# 리스트의 확장
"""
extend() 함수는 리스트의 요소를 늘려준다
(리스트에 리스트를 붙인다.)
리스트이름.extend(리스트)
리스트이름 = 리스트이름 + 붙이는리스트
"""
"""
myList2 = ['apple', 'a', 'b', 'b', 'c', 'bear']
myList2.extend(["web", "program"])

"""
myList2 = ['apple', 'a', 'b', 'b', 'c', 'bear']
myList2 += ["web", "program"]
# myList2 = myList2 + ["web", "program"]
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
#t[1] = 'yellow'
#del t[1]
print(t[1:])

# 튜플 합치기(+)와 여러번 이어쓰기(*)
"""
튜플의 데이터는 수정할 수 없지만
튜플 자체는 합치거나 여러번 합칠 수 있다.
"""

t = ('red', 'green', 'blue')
t2 = ('pink',)
t = t + t2
print(t)

# 튜플과 리스트 간의 자료 형변환
"""
튜플의 요소 값은 수정 할 수 없으므로
리스트로 변환하면 요소 값을 수정할 수 있다.

리스트를 튜플로 형변환 >> 변수이름 = tuple(리스트)
튜플을 리스트로 형변환 >> 변수이름 = list(튜플)

리스트 혹은 튜플을 집합으로 형변환
>> 변수이름 = set(리스트 혹은 튜플)
"""

# 리스트를 튜플로 형변환 > 튜플을 리스트로 형변환
l = ['a','b','c']
print(type(l))

t = tuple(l)
print(type(t))

t = ('a','b','c')
print(type(t))

# 튜플을 리스트로 형변환 > 리스트를 튜플로 형변환 
l = list(t)
print(type(l))

l[2]='d'
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

dic = {"name" : "pey", "a":"0119993323", 2 : "hello"}
dic["a"] = "파이썬"
print(dic)

# 딕셔너리에 값 추가하기
"""
딕셔너리이름[새로 넣을 키] = 새로 넣는 값
키-값 쌍에서 키를 중복 하여 넣으면

이전 키에 대응되는 값을 덮어쓴다.
키-값 쌍에서 값은 중복이 가능하다.
(키로 구분할 수 있기 때문에)
"""
dic["red"] = "빨강색"
print(dic)

# 딕셔너리에 값 제거하기
del dic["red"]
print(dic)

# 키 혹은 값을 따로 얻어오는 함수

"""
키 ) 변수 = 딕셔너리이름.keys()
값 ) 변수 = 딕셔너리이름.values()
쌍 ) 변수 = 딕셔너리이름.items()
"""
print("\n"*5)
k = dic.keys()
print(k)

v = dic.values()
print(v)

i = dic.items()
print(i)

# 딕셔너리를 비우는 함수 clear()

#dic.clear()
print(dic)

# 값을 가져오는 함수 get()
"""
dic["안녕하세요"]
dic.get("안녕하세요")
"""
"""
get함수는 값을 가져올 수 있다.
키에 맞는 값이 없을 경우 기본값을 설정할 수 있다.
"""
print(dic)
print(dic.get("배고파요", "해당 키에 대한 값이 없습니다.")
)

# 키 값이 있는지 확인하는 키워드 in
"""
딕셔너리 안에 키가 있는지 확인 할 수 있다.
검색할 키 in 딕셔너리 이름
결과는 True 혹은 False 로 나타난다.
"""
print("name" in dic)

"""
input_str1 = input()
input_str2 = input()

sp1 = input_str1.split(":")
sp2 = input_str2.split(":")

# 철수:100
score_dic = {}
score_dic[sp1[0]] = sp1[1]
score_dic[sp2[0]] = sp2[1]
score_dic["반평균"] = (int(sp1[1]) + int(sp2[1]))/2

print(score_dic)
"""


"""
name1, score1 = input(), int(input())
name2, score2 = input(), int(input())
score_dic = {name1:score1, name2:score2,
             "반평균":(score1+score2)/2}
print(score_dic)
"""

# 집합(SET)
"""
데이터를 저장 할 수 있지만
- 데이터간에 중복이 없고,
- 순서가 없다(인덱스를 쓸 수 없다)
집합은 괄호({})를 활용하여 만들 수 있다.
"""
s = {1,2,3,1}
print(s)

# 교집합 구하기
"""
&, intersection()
"""
s1 = {2,4,6,8,10}
s2 = {3,6,9,12,15}

s3 = s1 & s2
s4 = s1.intersection(s2)
print(s3)
print(s4)

# 합집합 구하기
"""
|, union()
"""
s3 = s1 | s2
s4 = s1.union(s2)
print(s4)


# 차집합
s1 = {2,4,6,8,10}
s3 = s1 - {8}
s4 = s1.difference({8})
print(s4)

# 집합에 값 추가/삭제하기
"""
한개의 집합 값을 추가하는 add(), 
여러개의 집합 값을 추가하는 update()
특정 값 제거하는 remove()
"""

s1.add(12)
print(s1)

s1.update([14,12,16])
print(s1)

s1.remove(16)
print(s1)


# 제어문 - if문
"""
조건에 따라 프로그램 흐름(실행)을 나눌 때
쓴다.
if 조건:
    참일때 실행하는 부분1
    참일때 실행하는 부분2
else:
    거짓일 때 실행하는 부분1
    거짓일 때 실행하는 부분2
    
if 다음에 실행하는 부분
주의) 참일 때 실행하는 부분은 탭 1번으로 들어쓴다.
"""

num = 1
if num == 2:
    print("20이 크다")
else:
    print("10이 크다")
"""
u_in = int(input())
if u_in > 20:
    print("입력한 숫자가 크다.")
else:
    print("입력한 숫자가 작다.")
"""
# if의 중첩
"""
if 혹은 else 의 실행 부분 안에
또다른 if 문을 넣을 수 있다.
"""
"""
u_in = int(input())
if u_in == 20:
    print("숫자 20을 입력했습니다.")
else:
    if u_in > 20:
        print("입력한 숫자가 크다.")
    else:
        print("입력한 숫자가 작다.")
"""
# 여러개의 조건을 쓰려면 and or를 활용한다.
"""
if u_in == 20 and u_in > 20:
    print("입력한 숫자가 크거나 같다")
else:
    print("입력한 숫자가 작다")
"""

# 조건을 비교할 때 리스트, 튜플, 문자열, 집합
# 딕셔너리 등을 쓸 수 있다.
if 'a' in ('b','c'):
    print("a가 있어요")
else:
    print("a가 없어요")
"""
집합 : 'x' in {'x','y'}
딕셔너리(키) : 'x' in 딕서녀리이름.keys()
딕셔너리(값) : 'x' in 딕서녀리이름.values()
"""

# elif (else if)
"""
if의 조건이 거짓인 후에 다시 다른 조건으로 비교할 때
elif를 쓴다

if 조건1:
    참일때 실행하는 부분1
    참일때 실행하는 부분2
elif 조건2:
    조건1이 거짓이고 조건2가 참일 때 실행하는 부분1
    조건1이 거짓이고 조건2가 참일 때 실행하는 부분2
elif 조건3:
    조건1,2이 거짓이고 조건3가 참일 때 실행하는 부분1
    조건1,2이 거짓이고 조건3가 참일 때 실행하는 부분2
else:
    조건 1,2,3 거짓일 때 실행하는 부분1
    조건 1,2,3 거짓일 때 실행하는 부분2
    
if 다음에 실행하는 부분
"""

# Tip) 난수 선택하기 

import random
num = random.randint(0,2)
print(num)

signal = num #int(input("숫자를 입력해주세요 : "))
if signal % 3 == 0:
    print("빨간불")
elif signal % 3 == 1:
    print("노란불")
else:
    print("초록불")


# while
"""
조건에 따라 특정 코드를 반복하는 반복문

while 조건:
    조건이 만족하면 실행되는 코드
다음 실행 코드
    
"""
"""
n_list = []
times = 0
while times < 10:
    n_list.append(int(input()))
    times = times + 1
    print("%d 번 동작하였습니다." % times)

print(n_list)
print("실행 종료")
"""
# 실행 흐름을 무조건 중단 하는 break.
# 조건부분으로 되돌아 가는 continue

times = 0
while False:
    times = times + 1
    print("%d 번 동작하였습니다." % times)
    if times == 1000:
        break

print("실행 종료")

times = 0
while times < 10:
    times = times + 1
    if times == 2:
        continue
    print("%d 출력 했습니다." % times)




580원 자판기
2단 출


    



