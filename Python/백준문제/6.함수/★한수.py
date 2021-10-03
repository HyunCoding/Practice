cnt = 0
for i in range(1, int(input())+1):
    if i < 100:
        cnt += 1
    elif (i//100)-(i % 100//10) == (i % 100//10)-(i % 10):
        cnt += 1
print(cnt)


# 숏코딩 확인해보기
#print(sum(i<100 or i//10%10*2==i%10+i//100 for i in range(1,int(input())+1)))
