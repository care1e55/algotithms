def ball(n):
    stairs = []
    stairs.append(1)
    stairs.append(1)
    stairs.append(2)
    for i in range(3, n+1):
        stairs.append(sum(stairs[i-3:i]))
    print(stairs[n])
ball(int(input()))