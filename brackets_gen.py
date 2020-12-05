from collections import deque

def gen(pos, a, stack):
    if (pos == n2) and not stack:
        print("".join(a))
        return
    if (pos < n2):
        a.append("[")
        stack.append("[")
        gen(pos+1, a, stack)
        a.pop()
        stack.pop()
        a.append("(")
        stack.append("(")
        gen(pos+1, a, stack)
        a.pop()
        stack.pop()
    if stack:
        if (stack[-1] == '['):
            a.append(']') 
            top = stack.pop()
            gen(pos, a, stack)
            a.pop()
            stack.append(top)
        elif (stack[-1] == '('):
            a.append(')')
            top = stack.pop()
            gen(pos, a, stack)
            a.pop()
            stack.append(top)

N = int(input())
n2 = N//2
arr = deque()
stack = deque()
gen(0, arr, stack)
