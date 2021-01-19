def poland(input_str):
    stack = []
    numbers = [str(i) for i in range(10)]
    for i in input_str.split():
        if i in numbers:
            stack.append(int(i))
            continue
        if i not in numbers:
            num_2, num_1 = stack.pop(), stack.pop()
            if i == "+":
                stack.append(num_1 + num_2)
            elif i == "-":
                stack.append(num_1 - num_2)
            elif i == "*":
                stack.append(num_1 * num_2)
    print(*stack)

poland(input())
