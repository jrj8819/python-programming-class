# Quiz) 거스름돈 동전 수 세기
"""
580원
500 1
100 0
50  1
10  3
1   0
"""
#money = int(input("거스름 돈을 입력해주세요 > "))
"""
동전 갯수를 저장하는 변수
"""
"""
coin_500 = 0
coin_100 = 0
coin_50 = 0
coin_10 = 0
coin_1 =0

while money >= 500:
    money -= 500 # money = money - 500
    coin_500 += 1 # coin_500 = coin_500 + 1

while money >= 100:
    money -= 100
    coin_100 += 1

while money >= 50:
    money -= 50
    coin_50 += 1

while money >= 10:
    money -= 10
    coin_10 += 1

coin_1 = money

print("500원 : %d\n100원 : %d\n50원 : %d\n10원 : %d\n1원 : %d\n" %
      (coin_500, coin_100, coin_50, coin_10, coin_1))
"""
# case 2)
"""
money = int(input("거스름돈을 입력해주세요 > "))

# key 0, 1, 2, 3, 4
# mean 500 100 50 10 1

emun_coins = { 0 : 500, 1 : 100, 2 : 50, 3 : 10, 4 : 1 }
check_coin = 0

count_coins = { 0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0 }

while True:
	if money >= emun_coins[check_coin]:
		count_coins[check_coin] = money // emun_coins[check_coin]
		money -= (count_coins[check_coin] * emun_coins[check_coin]) 
	
	check_coin += 1

	if money <= 0:
		break;

print("500원 : %d\n100원 : %d\n50원 : %d\n10원 : %d\n1원 : %d\n" % (
	count_coins[0], count_coins[1], count_coins[2], count_coins[3], count_coins[4]))
"""

# while 에서 무한 루프
"""
while 문의 조건 부분에 True를 주어 (프로그램을 강제 종료 시키기 전까지)
무한으로 동작 시킬 수 있다
다만 반복 동작이 마무리 되면 if 와 break를 활용하여
무한 루프를 종료한다.
"""
"""
user_input = []

while True:
    temp = input("횟수 제한 없이 입력을 받는 프로그램")
    if temp == "-1":
        break
    else:
        user_input.append(temp)
print(user_input)
"""

# Quiz
"""
문자 'q'를 입력하기 전까지 숫자를 입력 받아 모두 더한 값을 출력하세요
"""
"""
number_sum = 0
while True:
    temp = input("q가 입력되기 전까지 입력을 받습니다 > ")

    if temp == 'q':
        print("합계는 %d 입니다" % number_sum)
        break
    else:
        number_sum = number_sum + int(temp)
"""

# for
"""
리스트, 문자열, 튜플, 딕셔너리 안에 요소를
반복된 코드로 다루기 편하도록 for문이 제공된다

for 변수(리스트 안의 요소를 저장하는 변수) in 리스트[문자열, 튜플, 딕셔니리]:
    반복 실행할 코드
    
"""
"""
a = [1,2,3,4]
idx = 0
while idx < len(a):
    print(a[idx+1])
    idx += 1       
"""
a = [1,2,3,4]
t = ('a','b','c')
s = "abcd"
d = {"key1":"value1","key2":"value2"}
for (i, j) in d.items():
    print(i)
    print(j)
    

# Quiz) for문을 활용하여 구구단 2단을 출력하세요
a = [1,2,3,4,5,6,7,8,9]

for i in a:
    print("%d x %d = %d" % (2, i, (2*i)))
    


a = [(1,2,3),(3,4,4),(5,6,5)]

for (i, j, k) in a:
    print(i)
    print(j)

# 두개의 리스트를 동시에 for문에서 활용하기
name = ["홍길동", "이순신", "유관순"]
math = [80, 100, 70]

for (n, m) in zip(name, math):
    print(n)
    print(m)

# 값과 인덱스를 동시에 for문에서 활용하기
for i, n in enumerate(name):
    print(i)
    print(n)


# break 와 continue
for i in name:
    print(i)
    break
print("=========")
for i in name:
    if i == "홍길동":
        continue
    else:
        print(i)

# 값의 범위를 나타내는 range()와 for

for i in range(10): #[0,1,2,3,4,5,6,7,8,9]
    print(i)


for i in range(5, 9): #[5,6,7,8]
    print(i)

"""
range(끝)
range(시작, 끝)
range(시작, 끝, 간격)
"""
for i in range(5, 20, 5): #[5,10,15]
    print(i)


# range()함수로 횟수를 표현하는 예
for i in range(10):
    print("%d 회 출력 하였습니다" % i)


#Quiz
"""
0 이 입력될 때까지 정수를 계속 입력받아
3의 배수와 5의 배수를 제외한 수들의 개수를 출력하는 프로그램을 작성하시오.
"""
"""
user_input = []

while True:
    temp = input("횟수 제한 없이 입력을 받는 프로그램")
    if temp == "0":
        break
    else:
        user_input.append(int(temp))

count = 0

for i in user_input:
    if i % 3 == 0:
        continue
    if i % 5 == 0:
        continue
    count = count + 1
    
print("3의 배수와 5의 배수가 아닌 수는 %d 개 입니다." % count)
"""
# 리스트 안에 for 문 포함하기
"""
for문의 계산 내용을 리스트 안에 포함하여
간단하게 자료를 가공 및 저장하는 방법

대괄호 안에 for 문을 다음과 같은 규칙으로 넣는다
[실행하고 싶은 코드 for 변수 in 리스트(튜플, 딕셔너리 등)]
"""
# case1)
a = []

for i in range(10):
    a.append(i)

# case2)
b = [i*100 for i in range(10)]

print(a)
print(b)


# Quiz
"""
주사위 놀이를 하다가 주사위를 10번 던져서
각 숫자가 몇 번씩 나왔는지 알아보려고 한다.
한번 던질 때마다 나온 주사위의 숫자를 입력받아서
각 숫자가 몇 번씩 나왔는지 횟수와 출현 확률을
출력하는 프로그램을 작성하시오.
"""

import random
picks = 5000
l = [random.randint(1, 6)  for i in range(picks)]

print(l)

times = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}
for num in l:
    if num == 1:
        times["1"] += 1
    elif num == 2:
        times["2"] += 1
    elif num == 3:
        times["3"] += 1
    elif num == 4:
        times["4"] += 1
    elif num == 5:
        times["5"] += 1
    else:
        times["6"] += 1

print(times)

prob = [ (i * 100) / picks for i in times.values() ]

print(prob)

# 함수
"""
자주 쓰는 명령어를 모아 놓은 것
- 유지보수(수정 혹은 오류에 대처)가 편하다.
- 기능을 호출하기 편하다.


매개변수(인수, argument) : 기능을 수행하기 위한 재료(데이터)
기능(알고리즘) : 함수가 특정 동작을 하기 위한 코드(로직)
결과물 : 기능이 동작한 결과 (결과 값이 없을 수도 있다)

def 함수의이름(인수1, 인수2, 인수3 ...):
    코드 작성
    return 코드의 결과(결과를 반환 하는 값)
"""

def addNumber(num1, num2):
    result = num1 + num2
    return result


print(addNumber(1, 2))

"""
함수를 호출하는 부분(addNumber(1, 2))에서
인수 값(1, 2)들은 순서대로
함수를 정의한 부분 (def addNumber(num1, num2):)의
인수(num1, num2)에 대입된다

함수에서 계산을 끝낸 결과를 return 하면
함수의 호출하는 부분(addNumber(1, 2))에 대입(치환)된다.
"""

# quiz
"""
숫자 0에서 n까지 덧셈을 구하는 함수를 만드세요
"""
n = 10
total = 0

for i in range(n+1):
    total = total + i
print(total)

def addToNum(num):
    total = 0

    for i in range(num+1):
        total = total + i

    return total

print(addToNum(10))


# 입력값이 없는 함수
"""
인자 값을 비워 놓는다. 메시지를 출력하는데 활용
"""
def printMsg():
    print("반갑습니다")

# 결과 값이 없는 함수
"""
함수에 리턴(return) 값이 없는 경우
"""


# 입력 값의 개수를 정확히 알 수 없는 경우

"""
매개변수의 갯수가 가변적이면 *를 활용하여
다수의 매개변수를 활용할 수 있다.
"""

def myFunc(*a):
    for i in a:
        print(i)

myFunc(1,2,3,4,5,6)
myFunc('a','b','c')

# 리턴 값이 여러 개 인 함수
"""
함수의 리턴값은 여러개가 될 수 있다.
단, 리턴값을 받는 변수도 여러개가 되어야 한다.
변수가 리턴값과 같지 않으면 튜플로 리턴된다.
"""
def myfunc3(a, c):
    print("기본값 예제 리턴합니다")
    return a, c
word1, word2 = myfunc3("한국", "함수") #(a, c)리턴 
print(word1)
print(word2)

# 인수의 기본값
"""
함수를 호출할 때 인수 값을 지정하지 않아도
자동으로 값이 정해지는 기본 값이 있다

기본값으로 지정한 인수는 마지막 순서에 넣는다
"""

def myfunc3(a,c, b="기본값"):
    print("기본값 예제 리턴합니다")
    return a, b, c
word1, word2, word3 = myfunc3("한국", "함수")
print(word1)
print(word2)
print(word3)


# Quiz
"""
‘@’문자를 10개 출력하는 함수를 작성 한 후 함수를
세 번 호출하여 아래와 같이 출력하는 프로그램을 작성하시오.

출력 예시
first
@@@@@@@@@@

second
@@@@@@@@@@

third
@@@@@@@@@@

호출 예시
print10Words("first")
print10Words("second")
print10Words("third")
"""
print("first")
print("@"*10)

print("second")
print("@"*10)

print("third")
print("@"*10)

def print10Words(word):
    print(word)
    print("@"*10)

print10Words("first")
print10Words("second")
print10Words("third")


# Quiz
"""
원주율을 3.141592로 디폴트 인수로 정의하고
원의 넓이를 구하는 함수를 작성하여
반지름을 입력받아 원의 넓이를 출력하는 프로그램을 작성하시오.
"""

r = 10
pi = 3.141592

area = pi * r * r

print(area)

def areaCircle(r, pi = 3.141592):
    area = pi * r * r
    return area
    
print(areaCircle(10))


# Quiz
"""
매개변수로 숫자를 입력받을 횟수(N)를 함수에 전달하고
이후 숫자를 N회 입력하여 저장한 리스트를
출력하는 inputNumber() 함수를 만드세요

호출 예시
inputNumber(4)

입력:1
입력:2
입력:3
입력:4

출력 예시
my = inputNumber(4)
print(my)

[1,2,3,4]
"""

# 함수 안의 변수의 범위(scope)
"""
함수 안에서 만든 변수는
변수가 함수 종료와 동시에 사라지기 때문에
함수가 종료된 이후에는 쓸 수 없다
"""
"""
def myfunc4():
    result = "뒤의 결과 입니다."
    
myfunc4()
print(result)
"""

temp = ""
def myfunc5():
    global temp
    temp = "결과 입니다"

myfunc5()
print(temp)
"""
함수 내에서 함수 밖에 만든 변수를
활용하려면 변수 이름 옆에 global 키워드를 붙인다
global 키워드가 붙은 변수는
함수 내에서 만든 변수가 아니기 때문에
함수가 종료되도 사라지지 않는다
"""

# 파일

# 파일 만들기
f = open("c:\song.txt", "w")
"""
파일을 읽고 쓰려면 파일의 위치(경로)와 이름를 알아야한다.
모드는 읽기(r), 쓰기(w), 이어쓰기(a)

파일을 만들 때
파일의 이름이 중복되는 경우(같은이름의 파일이 존재)
내용이 넣어 써진다.
같은 파일이 없으면 새로운 파일이 만들어 진다.

open()의 결과물(리턴 값)으로 파일 객체
데이터를 파일로 쓰는 동작을 하는 대상
"""
f.write("동해물과\n백두산이")
"""
파일 객체에게 데이터를 전달하는 함수
f.write(쓰고 싶은 내용(데이터)
"""
f.close()
"""
데이터를 전달 후에는
파일 객체를 제거하는 f.close()함수를 호출한다
"""


# 파일 읽기
f = open("c:\song.txt", "r")
line = f.read()
f.close()
print(line)


"""
read() > 문자열을 모두 가져온다.
readlines() > 문자열을 모두 가져오지만, 라인별로 구분하여
                리스트로 가져온다.
readline() > 한 줄만 가져온다. 마지막 줄이면 return 값이 None
"""

print("="*10)

f = open("c:\song.txt", "r")
while True:
    line = f.readlines()
    if not line:#None
        break
    print(line)
f.close()


f = open("c:\song.txt", "r")
line = f.readline()
print(line)
f.close()

# Quiz
"""
1) 5명의 학생 점수를 입력받아 점수를 파일(test1.txt)로 저장하세요

2) 1에서 저장한 파일을 읽어와
점수, 등수를 파일로 출력하는 프로그램을 작성하시오.
단, Score는 5칸(%5d), Rank는 각 4칸(%4d)으로
파일(test2.txt)로 출력한다.
"""

st = []

for i in range(5):
    st.append(int(i))

print(st)
"""
문자열 앞에 r을 붙이면 보이지 않는 문자열 관련
라인피드 문자(제어문자)를 제거 할 수 있다.

경로 에러시 문자열 앞에 붙여주세요
"""
f = open(r"c:\test1.txt", "w")
for i in st:
    f.write("%d\n" % i)
f.close()

























      
