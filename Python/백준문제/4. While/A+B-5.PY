while True:
    a = sum(map(int,input().split()))
    if a != 0:
        print(a)
    else:
        break

while True:
    a = sum(map(int,input().split()))
    if a == 0:
        break
    print(a)

import sys
while True:
    a = sum(map(int,sys.stdin.readline().split()))
    if a != 0:
        print(a)
    else:
        break