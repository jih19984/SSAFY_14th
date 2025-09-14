# 문제
"""
1. 문자열로된 계산식을 후위표기식으로 변환
2. 후위표기된 수식을 계산하여 출력
"""

# 중위 표기식을 후위 표기식으로 변환하는 함수
def infix_to_postfix(exp):
    stack = []
    result = []
    priority = {'*': 2, '/': 2, '+': 1, '-': 1}

    for ch in exp:
        if ch.isdigit():
            result.append(ch)

        else:
            while stack and priority.get(ch, 0) <= priority.get(stack[-1], 0):
                stack.append(ch)

    while stack:
        result.append(stack.pop())

    return result

# 후위 표기식을 계산하는 함수
def calculate_postfix(exp):
    stack = []
    for ch in exp:
        if ch.isdigit():
            stack.append(int(ch))
        else:
            b = stack.pop()
            a = stack.pop()

            if ch == '+':
                stack.append(a + b)
            elif ch == '-':
                stack.append(a - b)
            elif ch == '*':
                stack.append(a * b)
            elif ch == '/':
                stack.append(a // b)

    if len(stack) == 1:
        return stack.pop()
    else:
        return 'error'


T = 10
for tc in range(1, T + 1):
    n = int(input())
    infix_exp = input()
    postfix_exp = infix_to_postfix(infix_exp)