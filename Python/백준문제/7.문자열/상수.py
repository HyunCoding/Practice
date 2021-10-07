a = input().split()
reverse = []
for i in a:
    hund = str(int(i)//100)
    ten = str(int(i)%100//10)
    one = str(int(i)%10)
    reverse.append(one+ten+hund)
print(max(reverse))


#숏코딩

print(max(input()[::-1].split()))