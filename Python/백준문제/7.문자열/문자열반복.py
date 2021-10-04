for i in [0]*int(input()):
    num, word = input().split()
    Sum_Word = []
    for j in word:
        Sum_Word.append(j*int(num))
    print(''.join(Sum_Word))


for i in [0]*int(input()):
    num, word = input().split()
    print(''.join([j*int(num) for j in word]))


# 리스트를 문자열로 합치기
# https://wikidocs.net/15559
