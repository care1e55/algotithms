def calc(n):
    d = []
    d.append(0)
    d.append(0)
    for i in range(2, n+1):
        case_1 = d[i-1] + 1
        if i%2 == 0:
            case_2 = d[int(i/2)] + 1
        else:
            case_2 = d[i-1] + 1

        if i%3 == 0:
            case_3 = d[int(i/3)] + 1
        else:
            case_3 = d[i-1] + 1

        d.append(min(case_1, case_2, case_3))
    print(d[-1])

calc(int(input()))