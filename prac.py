N=int(input())

answer=0

for i in range(N):
    word = input()
    for j in range(len(word)):
        if j!=len(word)-1:
            if word[j]==word[j+1]:
                pass
            elif word[j] in word[j+1:]:
                break
        else:
            answer+=1
print(answer)


----

n = int(input())
for i in range(n):
    word = input()
    for j in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i] in word[i+1:]:
                n -= 1
print(n)