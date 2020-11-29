import numpy as np

def calcanswer(n):
    d = []
    o = []
    d.append(0)
    d.append(0)
    o.append("")
    o.append("")
    for i in range(2, n+1):
        case_1 = d[i-1] + 1
        # print(i, i%2, i%3)
        if i%2 == 0:
            case_2 = d[int(i/2)] + 1
        else:
            case_2 = d[i-1] + 1

        if i%3 == 0:
            case_3 = d[int(i/3)] + 1
        else:
            case_3 = d[i-1] + 1

        
        d.append(min(case_1, case_2, case_3))

        am = np.argmin([case_1, case_2, case_3])
        if am == 0:
            o.append(o[i-1 ]+ str(1))
        if am == 1:
            o.append(o[int(i/2)] + str(2))
        if am == 2:
            o.append(o[int(i/3)] + str(3))
    print(o[-1])

calcanswer(int(input()))
