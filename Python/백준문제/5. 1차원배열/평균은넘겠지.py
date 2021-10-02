for i in range(int(input())):
    a = list(map(int, input().split()))
    aver = sum(a[1:])/a[0]
    cnt = 0
    for i in a[1:]:
        if i > aver:
            cnt += 1
    # format형식으로 자리수 조절
    print("{:.3f}%".format(cnt/a[0]*100))
    # f-string
    print(f"{cnt/a[0]*100:.3f}%")


# 숏코딩 활용할만한 거
for T in range(int(input())):
    n, *l = map(int, input().split())
    s = sum(l)/n
    print('%.3f%%' % (sum(i > s for i in l)*100/n))
