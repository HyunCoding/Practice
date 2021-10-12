# 1 = 1
# 2 - 7 = 2     5개   1+ 6* 1 ans
# 8 - 19 = 3    11개    1+ 6* 3     2 (plus)
# 20 - 37 = 4   17개    1+ 6* 6     3
# 38 - 61 = 5   23개    1+ 6* 10    4
#       90        29        1+ 6* 15    5

a = int(input())
ans = 1
plus = 1
if a == 1:
    print('1')
else:
    while 6*ans+1 < a:
        plus += 1
        ans = ans+plus
    print(plus+1)


# 검색코딩 1
n = int(input())
nums_pileup = 1  # 벌집의 개수, 1개부터 시작
cnt = 1
while n > nums_pileup:
    nums_pileup += 6 * cnt  # 벌집이 6의 배수로 증가
    cnt += 1  # 반복문을 반복하는 횟수
print(cnt)

# 검색코딩 2
n = int(input())
nums_pileup, cnt = 1, 1
while n > nums_pileup:
    nums_pileup += 6*cnt
    cnt += 1
print(cnt)
