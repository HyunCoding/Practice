# 백준 11021

import sys
for i in range(int(input())):
    print("Case #{}: {}".format(i+1, sum(map(int, input().split()))))

# ---------------------------------------------------------------------
# sys.stdin.readline() 활용하기

num = int(input())
for i in range(num):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #{}: {}".format(i+1, a+b))

# ★★★이해는 못했지만 어떻게 쓰는지 공부하기★★★
# open() , f-string
i = 0
for a, _, c, _ in [*open(0)][1:]:
    i += 1
    print(f'Case #{i}:', int(a)+int(c))

# ★★★이해는 못했지만 어떻게 쓰는지 공부하기★★★
# exec() , eval() , f-string
i = 1
exec('print(f"Case #{i}:",eval("+".join(input())));i+=1;'*int(input()))
