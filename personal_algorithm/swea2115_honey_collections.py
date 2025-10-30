# 문제
"""
N x N개의 벌통이 정사각형 모양을 배치되어 있음

각 벌통에 있는 꿀의 양이 주어졌을 때, 벌꿀을 채취하여 최대한 많은 수익을 얻으려고 한다.

<규칙>
1. 두 명의 일꾼이 있다. 꿀을 채취할 수 있는 벌통의 수 M이 주어질 때,
각각의 일꾼은 가로로 연속되도록 M개의 벌통을 선택하고, 선택한 벌통에서 꿀을 채취할 수 있다.
단 두명의 일꾼이 선택한 벌통은 서로 겹치면 안된다.

2. 두 명의 일꾼은 선택한 벌통에서 꿀을 채취하여 용기에 담아야 한다.
단, 서로 다른 벝통에서 채취한 꿀이 섞이게 되면 안된다. -> 하나의 벌통에서 채취한 꿀은 하나의 용기에 담자

3. 두 일꾼이 채취할 수 있는 꿀의 최대 양은 C (모두 적용)

4. 채취한 꿀의 상품가치는 각 용이게 있는 꿀의 양의 제곱만큼 수익이 생긴다.

벌통들의 크기 N, 
벌통에 있는 꿀의 양에 대한 정보, 
선택할 수 있는 벌통의 개수 M, 
꿀을 채취할 수 있는 최대 양 C가 주어질 때,

두 일꾼이 꿀을 채취하여 얻을 수 있는 수익의 합이 최대가 되는 경우를 찾고 최대 수익을 출력해라!
"""

# 풀이 방법
"""
우선 각 변수들의 범위 확인
- 3 <= N <= 10
- 1 <= N <= 5
- N <= M
- 10 <= C <= 30

-> 깊이 자체가 10밖에 안되므로 깊이 탐색으로 접근

1단계
1. dfs 함수 생성
2. 만약 값이 더 크다면 갱신

2단계
같은 행에 2명의 일꾼이 모두 채취하는 경우도 고려해야함!
"""
import sys
input = sys.stdin.readline

def dfs(idx, row_num):
    global N, M, C, check

    # 일꾼 2명이 끝났다면
    if check == 0:
        best = max(profit, best)

    for row in range(row_num, N):
        for i in range(idx, N-M+1):
            check -= 1
            price = 0
            for j in range(i, M+i):
                price = price + (honey_arr[row][j])
                profit = profit + (honey_arr[row][j] ** 2)
            if price > C:
                price = 0
                dfs(idx + 1, row_num + 1)
            else:
                dfs(idx + 1, row_num + 1)


N, M, C  = map(int, input().split())
check, profit = 1, 0
best = float('-inf')
honey_arr = [list(map(int, input().split())) for _ in range(N)]
dfs(0, 0)