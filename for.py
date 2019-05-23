"""
Quiz) elif 를 활용하여 입력한 숫자가 
90 이상 100 이하 "A"
80 이상 90 미만 "B"
80 미만 "non pass"
100 초과 
"잘못 입력하셨습니다."
출력하세요
90 <= num1 <= 100 (X) 
90 <=num1 and num1 <=100 (0)
"""
"""
iNum = int(input())
if iNum > 100:
    print("잘못 입력하셨습니다.")
elif iNum >= 90 and iNum <= 100:
    print("A")
elif iNum >= 80 and iNum < 90:
    print("B")
elif iNum < 80:
    print("non pass")
else
    pass
"""
# while

times = 0
while False:
    times = times + 1
    print("%d 번 동작하였습니다." % times)
    if times == 1000:
        break

print("실행 종료")
    

# Quiz) 다음과 같이 구구단 2단을
# 출력하는 프로그램을 작성하세요
"""
num1 = 2
num2 = 1
max_times = 9
times = 1
while times <= max_times:
    print("%d x %d = %d" % (num1, num2, num1*num2))
    times = times + 1
    num2 = num2 + 1
"""
"""
dan = 2
dan_max = 9
num2 = 1
num2_max = 9

while dan <= dan_max:
    while num2 <= num2_max:
        print("%d x %d = %d" % (dan, num2, dan*num2))
        num2 = num2 + 1

    num2 = 1
    dan = dan + 1
    print("="*10)
"""
"""
times = 0
while times < 10:
    times = times + 1
    if times == 2:
        continue
    print("%d 출력 했습니다." % times)
"""

# Quiz) 다음 코드에서 3, 6, 9회를 생략
# 다시 > 코드 수정 완료
"""
num1 = 2
num2 = 1
max_times = 9
times = 1
while times <= max_times:
    if times % 3 == 0:
        num2 = num2 + 1
        times = times + 1    
        continue
    print("%d x %d = %d" % (num1, num2, num1*num2))
    num2 = num2 + 1
    times = times + 1 
"""

# Quiz)2~9 단 코드
"""
dan = 2
dan_max = 9
num2 = 1
num2_max = 9

while dan <= dan_max:
    while num2 <= num2_max:
        if num2 % 3 == 0:
            num2 = num2 + 1
            continue
        print("%d x %d = %d" % (dan, num2, dan*num2))
        num2 = num2 + 1

    num2 = 1
    dan = dan + 1
    print("="*10)
"""

l = ['a','b','c']
t = ('a','b','c')
s = "abc"
d = {"key1":"value1","key2":"value2"}
#print(d.items())
for i in l:
    print(i)
    
print("="*10)
      
times_max = len(l)
times = 0
while times < times_max:
    print(l[times])
    times = times + 1



# Quiz) for 문을 활용하여 2단을 출력하세요
"""
l = [1,2,3,4,5,6,7,8,9]
l2 = [1,2,3]

for i, j in l, l2:
    print(i)
    print(j)
"""
#range()함수
"""
for i in "abcdef":
    print("2 x %s = %s" % (i, 2*i))
"""

# Quiz 학급의 10명의 학생의 중간고사 평균을 구하세요
# 교제 p139
# tatal += () >> total = total + ()



















































