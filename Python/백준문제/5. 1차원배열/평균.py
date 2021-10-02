a = int(input())
b = list(map(int, input().split()))
sum = 0
for i in range(a):
    sum += (b[i]/max(b)*100)
print(sum/a)


input()
a = list(map(int, input().split()))
print(sum(a)/len(a)/max(a)*100)
