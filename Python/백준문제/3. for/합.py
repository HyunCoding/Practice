# 백준 8393
n = int(input())
print(n*(n+1)//2)

# for문으로 풀기
a = 0
for i in range(1, int(input())+1):
    a += i
print(a)
