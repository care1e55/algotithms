import copy

def food_path(table, m, n):

    temp_table = copy.deepcopy(table)
    for i in range(m):
        for j in range(n):
            temp_table[i][j] = 0

    if m == 1 and n ==1:
        print(table[0][0])
        return 0

    temp_table[m-1][n-1] = table[m-1][n-1]

    for i in range(m-2,-1,-1):
        temp_table[i][n-1] = temp_table[i+1][n-1] + table[i][n-1]

    for i in range(n-2,-1,-1):
        temp_table[m-1][i] = temp_table[m-1][i+1] + table[m-1][i]

    for i in range(m-2,-1,-1):
        for j in range(n-2,-1,-1):
            temp_table[i][j] = min( temp_table[i+1][j], temp_table[i][j+1]) + table[i][j]

    i = 0
    j = 0
    path = table[0][0]

    while ((i!=(m-1)) and (j!=(n-1))):
        if temp_table[i+1][j] > temp_table[i][j+1]:
            j+=1
        else:
            i+=1
        path += table[i][j]

    if (i==(m-1)) and (j!=(n-1)):
        for k in range(j+1, n-1):
            path += table[i][k]

    if (j==n-1) and (i!=m-1):
        for k in range(i+1, m-1):
            path += table[k][j]

    path+= table[m-1][n-1]

    print(path)


m_and_n = input()
m = int(m_and_n.split()[0])
n = int(m_and_n.split()[1])
table = []

for i in range(m):
    line = input()
    table.append([int(j) for j in line.split()])

food_path(table, m, n)