def fibo(n):
    f = 1
    f1 = 1
    f2 = 1
    for i in range(1, n+1):
        if i < 3:
            continue
        else:
            f = f1 + f2
            f2 = f1
            f1 = f
    print(f)
fibo(int(input()))