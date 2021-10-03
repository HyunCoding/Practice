# 문제풀이 https://wook-2124.tistory.com/252

mlilon = set(range(1, 10001))
selfNum = set()

for i in mlilon:
    for j in str(i):
        i += int(j)
    selfNum.add(i)

ans = sorted(mlilon - selfNum)

for i in ans:
    print(i)

# set을 이용한 중복제거
# (set은 집합 자료형이다. set의 특징 자료의 순서가없고 중복을 허용하지않는다. )
# https://wikidocs.net/1015#update

# sorted 함수를 이용한 정렬
# (정렬된 결과는 list로 반환한다)
# https://blog.naver.com/timtaeil/221426580068
