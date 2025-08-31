# 문제
"""
수식의 길이: N (항상 홀수)
0 ~ 9의 정수, 연산자 (+, -, x)로 수식이 이루어짐
괄호 안에 들어있는 식은 먼저 계산(단, 괄호 안에 연산자 1개)

수식이 주어졌을 때 괄호를 적절히 추가해 만들 수 있는 식의 결과의
최댓값을 구하는 프로그램을 작성하시오

중요! 연산자의 우선순위가 모두 동일
-> 앞에서부터 차례대로 연산

<Input>
- N
- 수식 ex) 3+8*7-9*2

<Output>
- 136
"""

# 풀이 방법
"""
앞에서부터 차례대로 연산을 한다는 것을 고려해볼 때,
괄호로 묶은 경우와 아닌 경우 큰 값을 찾고 다음 단계로 넘어감 -> 똑같이 반복
3으로 시작
3 -> 3 + 8 or 3 + (8 * 7) 
11 * 7 -> 77 - 9, 77 - (9*2)
77 - 9 -> 68 * 2
"""
import sys

def calculator(x, y, op): # 연산 함수
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    
def dfs(idx, cur):
    global max_value

    # dfs 종료 조건: 수식을 전부 순회했을 때
    if idx == exp_len:
        max_value = max(max_value, cur)
        return

    # 앞에서부터 차례대로 더하는 경우
    nxt_value = calculator(cur, int(exp[idx+1]), exp[idx])
    dfs(idx + 2, nxt_value)

    # 뒤에를 괄호로 묶어서 먼저 계산하는 경우
    if idx + 4 <= exp_len:
        bracket_value = calculator(int(exp[idx+1]), int(exp[idx+3]), exp[idx+2])
        nxt_value = calculator(cur, bracket_value, exp[idx])
        dfs(idx + 4, nxt_value)
    
input = sys.stdin.readline
N = int(input().strip()) # boj에서 input값에 개행문자가 포함되어 있었는지 strip 없으면 런타임에러...
exp = input().strip()
max_value = -2**30 # 왜 max value를 0으로 두지 않았을까?
exp_len = len(exp)

dfs(1, int(exp[0]))

print(max_value)