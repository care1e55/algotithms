from collections import deque

open_brackets = ['[', '(']
brackets = ['[', '(', ']', ')']

def gen(pos, a, stack):
    if (pos == N):
        if not stack:
            # pass
            print("".join(a))
        return
    for i in brackets:
        if i in open_brackets:
            if len(stack) >= n2:
                continue
            a.append(i)
            stack.append(i)
        elif not stack:
            continue
        elif ((stack[-1] == '[' and i != ']') or
              (stack[-1] == '(' and i != ')')):
              continue
        else:
            a.append(i)
            top = stack.pop()
        gen(pos+1, a, stack)
        if i in open_brackets:
            stack.pop()
        else:
            stack.append(top)
        a.pop()

N = int(input())
n2 = N//2
arr = deque()
stack = deque()
gen(0, arr, stack)