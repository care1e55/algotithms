l = 0
r = 0
s = input()
z = [0]*len(s)
for i in range(1, len(s)):
    z[i] = max(0, min(z[i-l], r - i))
    while (i+z[i] < len(s)) and (s[i+z[i]] == s[z[i]]):
        z[i] += 1
    if (i + z[i]) > r:
        l = i
        r = i + z[i]
z[0] = len(s)
print(*z)