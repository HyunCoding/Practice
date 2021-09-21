# 백준 15552

# 참고사항 sys.stdin.readline
# https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline

import sys
for i in range(int(input())):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)


# 숏코딩1
print(*[sum(map(int, l.split()))for l in sys.stdin][1:])

# 숏코딩2
input()
for _ in sys.stdin:
    print(sum(map(int, _.split())))
