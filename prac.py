# exec(int(input()) * "p, *l=map(int, input().split())
#      print(f'{sum(p*i>sum(l)for i in l)/p:.3%}')
#      ")

for T in range(int(input())):
    n, *L = map(int, input().split())
print(n)
print(L)
s = sum(L)/n
print('%.3f%%' % (sum(i > s for i in L)*100/n))
