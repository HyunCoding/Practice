h, m = map(int, input().split())
if h != 0:
    if m < 45:
        print(h-1, m+15)
    elif m >= 45:
        print(h, m-45)
    else:
        print(h-1, 15)
elif h == 0:
    if m < 45:
        print(23, m+15)
    elif m >= 45:
        print(h, m-45)
    else:
        print(23, 15)


1)
h, m=map(int, input().split())
if m > 44:
    print(h, m-45)
elif m < 45 and h > 0:
    print(h-1, m+15)
else:
    print(23, m+15)


2)
h, m=map(int, input().split())
print((h-(m < 45)) % 24, (m-45) % 60)
# (m-45) % 60 = 59
# 음수를 양수로 나눴을때 나머지 이해가 잘안됨ㅜㅜ

3)
H, M=map(int, input().split())
if M < 45:  # 분단위가 45분보다 작을 때
    if H == 0:  # 0 시이면
        H=23
        M += 60
    else:  # 0시가 아니면 (0시보다 크면)
        H -= 1
        M += 60

print(H, M-45)
