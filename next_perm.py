def next_permutation(string):
    for i in range(len(string)-2, -1, -1):
        if string[i] < string[i+1]:
            pos = i + 1
            for j in range(i+1, len(string)):
                if (string[j] > string[i]) and (string[j] <= string[pos]):
                    pos = j
            string[i], string[pos] = string[pos], string[i]
            string[i+1:] = string[:i:-1]
            return "".join(string)
    return "".join(string[::-1])

while True:
    try:
        string=input()
        print(next_permutation(list(string)))
    except EOFError:
        break