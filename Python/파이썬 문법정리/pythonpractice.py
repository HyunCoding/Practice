# 백준 3052
# a = []
# for i in range(10):
#     a.append(int(input()) % 42)
# print(len(set(a)))


# 백준 1546
# 1)내가푼거
# a = int(input())
# b = list(map(int, input().split()))
# c = max(b)
# sum = 0
# for i in range(a):
#     sum += b[i]/c*100
# print(sum/a)

# 2)숏코딩
# input()
# a = list(map(int, input().split()))
# print(sum(a)/len(a)/max(a)*100)

# 참고사항
# list = [10,20,30]
# sum(List) = 60
# len(list) = 3
# max(list) = 30


# 백준 8958
# a = int(input())
# for i in range(a):
#     b = input()
#     s = list(b)
#     sum = 0
#     c = 1
#     for i in s:
#         if i == 'O':
#             sum += c
#             c += 1
#         else:
#             c = 1
#     print(sum)


# 백준 4344
# a = int(input())
# for i in range(a):
#     arr = list(map(int, input().split()))
#     avg = sum(arr[1:])/arr[0]
#     count = 0
#     for i in range(arr[0]):
#         if avg < arr[i+1]:
#             count += 1
#     print("{:.3f}%".format(count/arr[0]*100))
# # 참고사항
# # https://ming-jee.tistory.com/124
