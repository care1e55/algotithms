def calcanswer(n):
    d = []
    d.append(0)
    d.append(0)
    for i in range(2, n+1):
        case_1 = d[i-1] + 1
        if i%2 == 0:
            case_2 = d[i//2] + 1
        else:
            case_2 = d[i-1] + 1

        if i%3 == 0:
            case_3 = d[i//3] + 1
        else:
            case_3 = d[i-1] + 1

        d.append(min(case_1, case_2, case_3))

    answer = ""
    i = n
    while (i > 1):
        if d[i] == (d[i-1]+1):
            answer = "1"+answer
            i -= 1 
            continue
        if (i%2 == 0) and d[i] == (d[i//2]+1):
            answer = "2"+answer
            i //= 2
            continue
        answer = "3"+answer
        i //= 3
    print(answer)

calcanswer(int(input()))
