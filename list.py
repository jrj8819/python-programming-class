#문자열에서 특정 문자를 찾아주는 find와 index의 차이
"""
문자열에서 찾는 문자가 없을 경우에는
find는 -1 값을 표시하고
index는 에러를 발생시킨다.
"""

a = '/'
print(a.join("월화수목금토일"))

a = "KoReA"
print(a.upper())

a = "kOReA"
print(a.lower())

str1 = "대한민국"
str2 = " 대한  민국 "

print(str2.lstrip())
print(str2.rstrip())
print(str2.strip())

a = "동해물과 백두산이"
print(a.replace("백두", "한라"))

print(str2.replace("  ", ""))

today = "2019-05-16"
print(today.split('-')[2])

# 문자열을 나누는 Split
"""
Split 명령어로 문자열을 나누면 조각이 리스트로 만들어져
표시된다. 각 조각의 데이터를 가져오려면
중괄호([]) 안에 인덱스를 활용하여 가져온다.
"""
# quiz) 2016-05-16-월요일을 나누어서 다음과 같이 년월일
# 요일을 별도로 저장하세요

day = "2016-05-16-월요일"
day_list = day.split('-')

print(day_list)

print(day_list[0])
print(day_list[1])
print(day_list[2])
#case 1) '월요일'에서 '요일'을 공백으로 바꾸기 
print(day_list[3].replace("요일", ""))
#case 2) '월요일'에서 첫 문자를 인덱스로 가져오기
print(day_list[3][0])
#case 3) '월요일'에서 첫 문자만 슬라이스하기
print(day_list[3][:1])

# 리스트 만들기
"""
리스트는 문자열, 숫자, 참/거짓, 리스트 등
여러가지 자료를 모아놓은 자료 구조이다.

리스트 안의 요소들을 중괄호([])로 묶어 표현한다.

리스트 안의 요소들은 인덱스를 활용하여 개별적으로 가져올 수 있다.

슬라이스를 활용하여 리스트의 인덱스 범위에 있는 요소들을
추려서 가져올 수 있다.
"""

week = ['월','화','수','목','금','토','일']

print(week[3])

print(week[:5])

# quiz) 리스트 안에 다음 다섯개의 숫자를 저장하고 그중 첫번째 세번째 다섯번째 숫자만 더하여 출력하세요

numbers = [15, 20, 33, 10, 9]
#sum_numbers = numbers[0] + numbers[2] + numbers[4]
sum_numbers = numbers[-5] + numbers[-3] + numbers[-1]
print(sum_numbers)


# 리스트 안에 요소로 리스트가 저장된 경우(중첩(Nested))에
# 요소 리스트의 데이터 접근하기

week2 = ['월','화','수','목','금',['토','일']]

good_day = week2[-1]
print(good_day[0])

print(week2[-1][0])


# quiz) 다음과 같은 리스트가 있을 때 나라 이름만 출력해주세요.
"""
case1)

 ["대한민국입니다", "미국에 어서오세요", ["일본", "중국", "태국입니다."] ]

case2)

 ["대한민국입니다", "미국에 어서오세요", ["일본, 중국, 태국입니다."] ]
"""
case1 = ["대한민국입니다", "미국에 어서오세요", ["일본", "중국", "태국입니다."]]       

kor = case1[0][0:4]
print(kor)

usa = case1[1][0:2]
print(usa)

jap = case1[2][0]
print(jap)

china = case1[2][1]
print(china)

tai = case1[2][2][0:2]
print(tai)

case2 = ["대한민국입니다", "미국에 어서오세요", ["일본, 중국, 태국입니다."] ]

jap = case2[2][0][0:2]
print(jap)

china = case2[2][0][4:6]
print(china)

tai = case2[2][0][8:10]
print(tai)


# 리스트 더하기 곱하기
"""
리스트 더하기는 2개의 리스트를 합치는 기능, 리스트의 요소값이 더해지지 않는다.

합쳐진 리스트에서 리스트의 요소는 중복이 허용된다.
"""

a = ['한국','중국','일본']
b = ['미국','멕시코','한국']

print(a+b)

print(a*3)


# 리스트의 요소 수정하기
"""
리스트의 값을 수정하기 위해서는 인덱스를 활용하여
특정 요소를 지정한다.
"""

a[2] = "Japan"
print(a)

a[1:2] = ["인도", "이라크"]
print(a)



# 키보드의 입력을 받는 명령어 input()
userInput = input()






































































