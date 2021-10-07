cnt = 0
countnum = []
for i in range(int(input())):
    word = input()
    setword = list(set(word))
    if len(word) == len(setword):
        cnt += 1
    else:
        for i in setword:
            countnum.append(word.count(i))
            num = setword[countnum.index(max(countnum))]
    
        #중복값의 인덱스 위치찾기
        #중복값 인덱스 비교
print(cnt)