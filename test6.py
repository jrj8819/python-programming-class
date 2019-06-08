# Quiz
1) 5명의 학생 점수를 입력받아
점수를 파일로 저장하세요

2) 1에서 저장한 파일을 읽어와
점수, 등수를 파일로 출력하는 프로그램을 작성하시오.
단, Score는 5칸(%5d), Rank는 각 4칸(%4d)으로
파일(test2.txt)로 출력한다.

with open('./test.txt', 'w') as f:
    while True:
        msg = input()
        if msg == "-1":
            break;
        else:
            f.write(msg+"\n")

table = []

with open('./test.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line: break

        table.append(int(line))

table.sort()
table.reverse()
print(table)


with open('./test2.txt', 'w') as f:
    f.write("%4s%5s\n" % ("score", "rank"))
    for i, v in enumerate(table):
        msg = "%4s%5s\n" % (str(v), str(i))
        f.write(msg)
print("파일이 만들어 졌습니다")

Quiz +)
5명의 학생 이름과 점수를 입력받아
이름과 점수, 등수를 파일로 출력하는 프로그램을
작성하시오.
단, 입력시 "이름", "점수", "등수"는
한 칸의 공백으로 구분을 하며,
Name은 4칸(%4s), Score는 5칸(%5d),
Rank는 각 4칸(%4d)으로 출력한다.
