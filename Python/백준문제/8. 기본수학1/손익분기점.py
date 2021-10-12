# 시간초과 / 시간제한 0.35
# a, b, c = map(int, input().split())
# cnt = 1
# while a+(b*cnt) >= c*cnt:
#     if b > c:
#         cnt *= 0
#         cnt -= 1
#         break
#     cnt = cnt+1
# print(cnt)

a, b, c = map(int, input().split())

if b >= c:
    print('-1')
else:
    print((a//(c-b))+1)
