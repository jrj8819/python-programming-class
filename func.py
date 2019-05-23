# Quiz) for 문을 이용하여
# A학급의 평균 점수를 구해보자.
A = [70,60,55,75,95,90,80,80,85,100]
total = 0
for num in A :
    #total = total + num
    total += num
average = total / len(A)
#print( average )

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

def helloWorld(name):
    print("hello world %s" % name)
  #  return name

helloWorld("래진")
msg = helloWorld("래진")
print(msg)

# 숫자를 하나 입력하고 1부터 입력한 숫자까지
# 더한 값을 반환하는 함수를 만들어 실행하세요
"""
userInput = int(input())

def addToNum(num):
    total = 0
    addNum = 1
    while addNum <= num :
        total = total + addNum;
        addNum = addNum + 1
    return total

def addToNumFor(num):
    # 숫자가 1000 넘는지 검사한다.
    if num > 1000:
        print("숫자가 너무 큽니다")
        return -1
    else:            
        # 숫자를 더한다.
        total = 0
        for i in range(1, num+1):
            total = total + i
            
        return total
    
result = addToNumFor(userInput)
print(result)
"""
"""
함수에서 return 키워드를 실행하면 함수의 return 값이
반환 된다. 또한 함수가 종료 된다.
그러므로 return 다음에 나오는 함수의 코드는 실행되지 않는다.

하나에 함수 안에서 if문으로 실행흐름을 분기하면
실행흐름마다 return 값을 활용할 수 있다
"""

def myFunc(*a):
    for i in a:
        print(i)

myFunc(1,2,3,4,5,6)

"""
매개변수의 갯수가 가변적이면 *를 활용하여
다수의 매개변수를 활용할 수 있다.
"""

def myFunc2():
    print("숫자 2개를 리턴합니다")
    return 1, 2

num1, num2 = myFunc2()
print(num1)
print(num2)

"""
함수의 리턴값은 여러개가 될 수 있다.
단, 리턴값을 받는 변수도 여러개가 되어야 한다.
변수가 리턴값과 같지 않으면 튜플로 리턴된다.
"""

def myfunc3(a,c, b="기본값"):
    print("기본값 예제 리턴합니다")
    return a, b, c
num1 = myfunc3("한국", "함수")
print(num1)

"""
기본값을 주는 매개변수는 가장 마지막에 순서로 배치한다.
사용자가 함수에 주어진 매개변수가 기본값을 넣는 것인지
일반 값을 넣는 것인지 모호하기 때문에
"""

# 함수 안의 변수의 범위(scope)
result = "결과입니다."
def myfunc4():
    global result
    result = result + "뒤의 결과 입니다."
    print(result)

myfunc4()
print(result)

"""
global 키워드를 사용한 변수는 함수가 종료 되어도
활용할 수 있다.
"""

# 파일
f = open("c:\song.txt", "r")
line = f.readline()
print(line)
f.close()

"""
파일을 읽으려면 파일의 위치(경로)를 알아야한다.
모드는 읽기(r), 쓰기(w), 이어쓰기(a)

open(파일 위치, "모드") 함수로 파일과 파이썬 간에
데이터를 주고 받는 터널(파이프, pipe)가 만들어 진다.

readline()함수로 파일의 한 줄을 읽어 올 수 있다.

마지막에는 파일을 close() 함수로 닫는다. 
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
line = f.read()
print(len(line))
f.close()

"""
read() > 문자열을 모두 가져온다.
readlines() > 문자열을 모두 가져오지만, 라인별로 구분하여
                리스트로 가져온다.
readline() > 한 줄만 가져온다. 마지막 줄이면 return 값이 None
"""


f = open("c:\애국가.txt", "w")
f.write("애국가 입니다.")
f.close()

"""
파일과 파이썬의 파이프를 쓰기(w)모드로 읽으면
파일에 내용을 쓸 수 있다.
파일이 중복되는 경우(같은이름의 파일이 존재) 내용이 넣어 써진다.
같은 파일이 없으면 새로운 파일이 만들어 진다.
"""

f = open("c:\애국가2.txt", "a")
f.write("뒤에 이어서 쓴 애국가 입니다.")
f.close()

"""
파일의 내용을 이어서 쓰려면 이어쓰기(a)모드로 파일을
설정한다.
같은 이름의 파일이 존재하면 그 파일의 내용을 이어 쓴다.
같은 파일의 이름이 없으면 새로 파일을 만든다.
"""






































































