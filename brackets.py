open_brackets = ['[', '(']
brackets = ['[', ']', '(', ')']

def checkstr(test_string):
    stack = []
    for i, char in enumerate(test_string):
        if char in brackets:
            if char in open_brackets:
                stack.append((i, char))
                continue
            if not stack:
                return False
            top = stack.pop(-1)
            if ((top[1] == '[' and char != ']') or
                    (top[1] == '(' and char != ')')):
                return False
    if stack:
        return False
    else:
        return True
    return True

def small_checkstr(test_string):
    stack = []
    for i, char in enumerate(test_string):
        if char in open_brackets:
            stack.append((i, char))
            continue
        if not stack:
            return False
        top = stack.pop(-1)
        if ((top[1] == '[' and char != ']') or
                (top[1] == '(' and char != ')')):
            return False
    return True

def gen(pos, N, a):
    if (pos == N):
        result = "".join(a)
        if checkstr(result):
            # print(result)
            stack = []
        return
    for i in brackets:
        a.append(i)
        if not small_checkstr(a):
            a.pop()
            continue
        gen(pos+1, N, a)
        a.pop()

arr = []
gen(0, int(input()), arr)