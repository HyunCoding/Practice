word = input().upper()
SetWord = list(set(word))
cnt_list = []
for i in SetWord:
    cnt_list.append(word.count(i))
if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    print(SetWord[cnt_list.index(max(cnt_list))])
