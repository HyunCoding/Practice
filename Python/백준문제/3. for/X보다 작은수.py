a,b=map(int,input().split())
c = list(map(int,input().split()))
for i in c:
    if b > i:
        print(i,end=" ")


# 다른사람 코딩
x,y=input().split()
print(*[i for i in input().split()if int(i)<int(y)])

n,x,*a=map(int,open(0).read().split())
for i in a:i<x!=print(i)

n=int(input().split()[1])
print(*[i for i in input().split()if int(i)<n])