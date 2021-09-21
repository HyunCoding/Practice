# 백준 9498

a = int(input())

if 101 > a > 89:
    print('A')
elif 90 > a > 79:
    print('B')
elif 80 > a > 69:
    print('C')
elif 70 > a > 59:
    print('D')
else:
    print('F')

숏코딩
문자열의 인덱스: 'str'[int]
print("FFFFFFDCBAA"[int(input())//10])

("FFFFFFDCBAA")
문자열의 길이 총 10
F F F F F F D C B A A
0 1 2 3 4 5 6 7 8 9 10

[int(input())//10]
입력받은 값을 10으로 나눈 몫
100을 받으면 10
92를 받으면 9
80을 받으면 8
77을 받으면 7

입력받은 값을 10으로 나눈 몫을 가지고 문자열의 인덱스로 매칭

ex) 입력받은 점수가 77일때
[int(input())//10]
(int(77)//10)
(77//10)
7

("FFFFFFDCBAA"[7])
문자열의 7번째값은 C
