# 백준 2742

# range함수 사용법
# https://withcoding.com/79

for i in range(int(input()), 0, -1):
    print(i)

# ----------------------------------------------

[print(i) for i in range(int(input()), 0, -1)]

# ----------------------------------------------

print(*range(int(input()), 0, -1))
