Quiz) 2이상의 숫자를 매개변수로 받아 다음과 같은 형태로 0부터 출력하는
함수를 구성하세요

size = int(input())

if size >= 2:
    max_number = size * size
    print_number = 0
    msg = ""
    for i in range(size):
        for j in range(size):
            msg += "%d\t" % (print_number)
            print_number += 1
        print(msg)
        msg = ""
        msg += "\n"
else:
    pass
