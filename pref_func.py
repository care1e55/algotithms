def pref_func(s):
    p = [0] * len(s)
    for i in range(1, len(s)):
        p[i] = p[i -1]
        while (p[i] > 0) and (s[p[i]] != s[i]):
            p[i] = p[p[i] - 1]
        if s[p[i]] == s[i]:
            p[i] += 1
    print(*p)
pref_func(input())