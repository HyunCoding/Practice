from string import ascii_lowercase
alphabet = list(ascii_lowercase)

b = input()
for i in alphabet:
    print(b.find(i), end=" ")

# ---------------------------------------------------------------

# 괜찮은코딩 숏코딩에서 가져옴
word = input()
alphabet = list(range(97, 123))  # 아스키코드 숫자 범위

# find함수 활용 (문자열에 해당하는 index를 리턴 , 없을시 -1 리턴)
# 문자 -> 아스키코드 : chr()
for x in alphabet:
    print(word.find(chr(x)))

# ---------------------------------------------------------------

# 문자열 포함관계 확인하는 2가지방법 + 특정 문자열로 시작하는지 확인하는법
# if "문자" in 문자열
# find()
# https://codechacha.com/ko/python-find-str-in-str/
