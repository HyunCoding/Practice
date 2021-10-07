cnt = 0
for i in input():
    n = ord(i)
    if n<68:cnt+=3
    elif n<71:cnt+=4
    elif n<74:cnt+=5
    elif n<77:cnt+=6
    elif n<80:cnt+=7
    elif n<84:cnt+=8
    elif n<87:cnt+=9
    else:cnt+=10
print(cnt)

#숏코딩
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
ret = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            ret += dial.index(i)+3
print(ret)

#숏코딩1,2
s = input()
a = '22233344455566677778889999'
r = 0
for i in s:
    r += int(a[ord(i)-65])+1
print(r)

print(sum(int('22233344455566677778889999'[ord(c)-65])+1 for c in input()))

#숏코딩3,4
print(sum(5*min(ord(x),88)//16-17for x in input()))

print(sum(min(ord(c)-64,25)*11//35+3for c in input()))

