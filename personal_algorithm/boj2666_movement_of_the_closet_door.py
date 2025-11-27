# 문제
"""
start: 16:00
end:
 
n개의 같은 크기의 벽장들이 일렬로 붙어져 있고,
벽장의 문은 n-2개만 있다.

한 벽장 앞에 있는 문은 이웃 벽장 앞에 문이 없다면,
그 벽장 앞으로 움직일 수 있다.

<풀어야 할 문제>
입력으로 주어지는 사용할 벽장 순서에 따라
벽장문을 이동하는 순서를 찾는 것!

이 때 벽장문의 이동횟수를 최소로 하여야 한다!

!!! 열린 벽장의 문이 2개 있는 것이 핵심 !!!

<입력>
1. 벽장의 개수 (3초과 20이하)
2. 두 개의 벽장을 나태내는 2개의 정수
3. 벽장들의 순서 길이 (최대 20)
이후 사용할 벽장의 번호를 한줄씩 입력
"""

# 풀이 방법
"""
예시를 한 번 보자
벽장 개수; 7, 열린 벽장의 번호: 2, 5
벽장들의 순서 길이: 4
벽장들의 순서: 3, 1, 6, 5

1. 2번 벽장을 3번으로 민다 : + 1 -> 3, 5
2. 3번 벽장을 1번으로 민다: + 2 -> 1, 5
3. 5번 벽장을 6번으로 민다: + 1 -> 1, 6
4. 6번 벽장을 5번으로 민다: + 1 -> 1, 5

그리디하게 한다면 항상 최소로 값이 보장될 것인가? 
무조건 보장이 된다. 벽장문은 일렬로 나열되어 있고, 정해진 순서에 따라 문을 열어야 하기 때문에!!
라고 생각했지만, 거리가 같은 경우 2가지를 모두 고려해야 한다!

3차원 dp 배열을 만들어서 각 배열의 요소에 (왼쪽, 오른쪽)를 넣는다.
"""

import sys

input = sys.stdin.readline

closet_numbers = int(input())
closet_list = list(map(int, input().split()))
closet_length = int(input())

# 요청할 벽장 시퀀스 전부 읽기
targets = [int(input()) for _ in range(closet_length)]

dp = [[[-1] * (closet_numbers + 1) for _ in range(closet_numbers + 1)] for _ in range(closet_length + 1)]

def dfs(idx, left, right):
    if idx == closet_length:
        return 0
    
    if dp[idx][left][right] != -1:
        return dp[idx][left][right]
    
    t = targets[idx]
    
    # 이미 열린 문 앞이면 비용 0으로 다음으로
    if t == left or t == right:
        dp[idx][left][right] = dfs(idx + 1, left, right)
        
    else:
        # 왼쪽 문을 이동시키는 경우, 오른쪽 문을 이동시키는 경우 중 최소 선택
        move_left = abs(t - left) + dfs(idx + 1, t, right)
        move_right = abs(t - right) + dfs(idx + 1, left, t)
        dp[idx][left][right] = min(move_left, move_right)
    return dp[idx][left][right]

start_left, start_right = closet_list

print(dfs(0, start_left, start_right))
