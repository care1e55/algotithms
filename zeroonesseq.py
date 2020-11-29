def zerooneseq(n):
    Fk1 = 1
    Fk2 = 2
    Fk = 2

    for i in range(2, n+1):
        Fk = Fk1 + Fk2
        Fk1 = Fk2
        Fk2 = Fk
    print(Fk)

zerooneseq(int(input()))