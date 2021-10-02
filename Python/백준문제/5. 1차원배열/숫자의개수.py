a = 1
for i in range(3):
    a *= int(input())
b = list(map(int, str(a)))
for i in range(10):
    print(b.count(i))


a = 1
for i in range(3):
    a *= int(input())
for i in range(10):
    print(str(a).count(str(i)))


# 파이썬 숫자 쪼개기
# # 10보다 큰 숫자는 간혹 숫자를 쪼개야하는 경우가 생긴다. 그럴 때 유용하게 사용할 수 있다.
# number,k = map(int,input().split()) # number =123
# number = list(map(int,str(number))) # number = [1,2,3]

# 카운트 함수
# https://ooyoung.tistory.com/76
