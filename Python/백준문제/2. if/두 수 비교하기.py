# 백준 1330

a, b = map(int, input().split())

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')

# 숏코딩
a, b = map(int, input().split())
print(['><'[a < b], '=='][a == b])
