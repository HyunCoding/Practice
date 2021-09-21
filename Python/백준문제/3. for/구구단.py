# 백준 2739

a = int(input())
for i in range(1, 10):
    print("{} * {} = {}".format(a, i, a*i))


a = int(input())
for i in range(1, 10):
    print(a, '*', i, '=', a*i)

# 숏코당인데.........
# i = 1
# n = int(input());
# exec("print(n,'*',i,'=',n*i);i+=1;"*9)
