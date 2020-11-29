def horse(n,m):
    deck = [[int(0) for i in range(m+2)] for j in range(n+2)]
    deck[2][2] = 1
    for i in range(2, n+2):
        for j in range(2,m+2):
            deck[i][j] += deck[i-2][j-1]
            deck[i][j] += deck[i-1][j-2]
    print(deck[n+1][m+1])
    return deck
inp = input()
deck = horse(*[int(i) for i in inp.split()])