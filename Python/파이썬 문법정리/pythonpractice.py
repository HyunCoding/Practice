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


# for i in range(int(input())):
#     b = list(input().split())
#     c = []
#     for i in b[1]:
#         c.append(i*int(b[0]))
#     print(''.join(c))

# for i in range(int(input())):
#     b = list(input().split())
#     c = ''
#     for i in b[1]:
#         c += (i*int(b[0]))
#     print(c)

# for i in [0]*int(input()):
#     print(i)
#     s = input().split()
#     print(''.join([x*int(s[0]) for x in s[1]]))

# t = int(input())
# for i in range(t):
#     num, s = input().split()
#     text = ''
#     for i in s:
#         text += int(num) * i
#         print(text)
#     print(text)


# input()
# sum = 0
# for i in input():
#     sum += int(i)
# print(sum)

# 숏코딩
# input()
# print(sum(map(int, input())))

# 참고자료
# https://go-hard.tistory.com/96


# from string import ascii_lowercase
# alpha = list(ascii_lowercase)
# b = input()

# for i in alpha:
#     if i in b:
#         print(b.index(i))
#     else:
#         print(-1)

# #참고자료
# #https://codechacha.com/ko/python-find-str-in-str/

# word = input()
# alphabet = list(range(97,123))  # 아스키코드 숫자 범위

# for x in alphabet :
#     print(word.find(chr(x)))  #find함수 활용

# #참고자료
# # https://ooyoung.tistory.com/78


# a = list(input().upper())
# cnt_list = []
# for i in set(a):
#     cnt_list.append(a.count(i))

# if cnt_list.count(max(cnt_list)) > 1:
#     print('?')
# else:
#     max_index = cnt_list.index(max(cnt_list))
#     print(a[max_index])


# print(len(input().split()))


# a = input().split()
# rever = []
# for i in a:
#     hund = str(int(i)//100)
#     ten = str((int(i) % 100)//10)
#     one = str((int(i) % 100) % 10)
#     rever.append(int(one+ten+hund))
# print(max(rever))

# #숏코딩
# 1)
# a,b=input().split()
# print(max(a[::-1],b[::-1]))

# 2)
# print(max(input()[::-1].split()))
