# 백준 2753
a = int(input())

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('1')
else:
    print('0')

# 숏코딩
a = int(input())
print(+((a % 100 or a//100) % 4 < 1))

# 숏코딩 참고사항
print(+(True)) = 1
print(+(False)) = 0
print(int(True)) = 1
print(int(False)) = 0
print(float(True)) = 1.0
print(float(False)) = 0.0
