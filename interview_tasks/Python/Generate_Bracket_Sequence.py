def generate_brackets(n):
    stack = ['(']
    result = []
    while stack:
        sequence = stack.pop()
        if len(sequence) == 2 * n:
            result.append(sequence)
        else:
            if sequence.count('(') < n:
                stack.append(sequence + '(')
            if sequence.count(')') < sequence.count('('):
                stack.append(sequence + ')')
    return result


print(*generate_brackets(int(input()))[::-1], sep='\n')
