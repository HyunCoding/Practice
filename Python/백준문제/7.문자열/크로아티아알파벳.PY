Word = input()
cnt = len(Word)
for i in '-','=','dz=','lj','nj':
    if i in Word:
        cnt -= Word.count(i)
print(cnt)

#검색해본 풀이방법
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
print(len(word))

# 참고사항 replace함수 문자열 제거,수정변환
# https://yuddomack.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-replace-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%A0%9C%EA%B1%B0-%EC%88%98%EC%A0%95%EB%B3%80%ED%99%98
