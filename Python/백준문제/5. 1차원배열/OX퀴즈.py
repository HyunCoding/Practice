for i in range(int(input())):
    sum = 0
    cnt = 0
    for i in list(input()):
        if i == 'O':
            sum += 1
            cnt += sum
        else:
            sum = 0
    print(cnt)
