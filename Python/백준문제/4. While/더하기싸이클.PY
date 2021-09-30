a = int(input())
num = a
cnt = 0
while True:
    ten = int(num)//10
    one = int(num)%10
    num = int(str(one)+str((ten+one)%10))
    cnt += 1
    if a == num:
        break
print(cnt)
