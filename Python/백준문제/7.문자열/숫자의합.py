input()
sum = 0
for i in input():
    sum += int(i)
print(sum)


# 숏코딩 밑에형식 생각보다 많이쓰임...
input()
print(sum(map(int, input())))
