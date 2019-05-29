# 예외처리
"""
프로그램이 동작하면서(사용자가 사용하면서) 발생하는
에러에 대해 대비하기 위한 방법

try:
    실행하는 코드
except 발생오류이름 as 오류메시지저장변수 :
    오류에 대처하는 코드
else:
    오류가 나지 않았을 때 코드
finally:
    오류 유무와는 별도로 무조건 실행되는 코드
    
발생오류종류
ZeroDivisionError : 0으로 나눈 경우
NameError : 변수명이 없는 경우
IndexError : 문자열, 리스트에서 인덱스 잘못 입력한 경

모든오류 종류 확인하는 링크
https://docs.python.org/ko/3/library/exceptions.html
"""
"""
try:
    num = int(input())
    print(100/num)
except ZeroDivisionError as e:
    print("%s 에러가 발생했어요 " % e)
else:
    print("정상적으로 계산되었습니다")
"""
try:
    f = open("c:\애국가2.txt", "r")
except FileNotFoundError as e:
    print("%s 에러가 발생했어요 " % e)
else:
    data = f.read()
    print(data)
finally:
    print("처리가 완전히 끝났습니다")

# 오류 발생시키는 키워드 raise
"""
특정 오류를 의도적으로 발생시켜
태스트하거나 프로그램적으로 예외 처리를 하는 키워드

raise 에러이름[FileNotFoundError, NameError 등]

주로 사용자가 정의한 에러를 발생시키는데 주로쓴다.
"""
#raise NameError

try:
    f = open("c:\애국가.txt", "r")
    raise FileNotFoundError
except FileNotFoundError as e:
    print("%s 에러가 발생했어요 " % e)
else:
    data = f.read()
    print(data)
finally:
    print("처리가 완전히 끝났습니다")

# 사용자 정의 예외
"""
사용자가 프로그램의 용도에 맞게
정의한 예외 처리
"""

class MyException(Exception):
    msg = "입력 내용이 남 혹은 여 이어야 합니다."

    def __str__(self):
        print(msg)

str1 = "남"
str2 = "woman"
"""
if str1 == "남" and str2 == "여":
    print("잘 입력하셨습니다.")
else:
    raise MyException
"""
# 자주쓰는 내장 함수
"""
1) enumerate
for 문에서 index와 값을 동시에 활용할 수 있다.
"""

nation = ["KOREA","USA","CHINA"]
for i, n in enumerate(nation):
    print("%d %s" % (i,n))
    


"""
2) lambda
간단한 계산의 함수를 축약하여 표현할 수 있다.

lambda 매개변수1, 매개변수2 : 매개변수1 + 매개변수2(간단한 계산)
"""

def sum1(n1, n2):
    return n1 + n2

sum2 = lambda n1, n2 : n1 + n2

print(sum1(1,2))
print(sum2(3,4))



"""
3) Map

특정 함수를 리스트에 적용할 때 활용한다.
"""
def two_times(mList):
    result = []
    for n in mList:
        result.append(n*2)
    return result

pList = two_times([1,2,3,4])

pList2 = list(map(lambda a : a*2, [1,2,3,4]))
print(pList)

print(pList2)














































    
