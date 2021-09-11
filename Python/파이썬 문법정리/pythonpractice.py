
# a = []
# for i in range(10):
#     a.append(int(input()) % 42)
# print(len(set(a)))


input()
a = list(map(int, input().split()))
print(sum(a)/len(a)/max(a)*100)

# 참고사항
# list = [10,20,30]
# sum(List) = 60
# len(list) = 3
# max(list) = 30
