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

# 가격의 최댓값을 구하는 함수
def get_max_price(x, y, cnt, honey_sum, price):
    global result
    if honey_sum > c:
        return
    result = max(result, price)
    if cnt == m:
        return
    # 현재 벌통을 선택
    get_max_price(x, y + 1, cnt + 1, honey_sum + grid[x][y], price + grid[x][y] ** 2)
    # 현재 벌통을 선택하지 않음
    get_max_price(x, y + 1, cnt + 1, honey_sum, price)


# 일꾼에 따라 최댓값을 구한 후 최종 가격 리턴
def solve(x, y):
    global result
    # 첫 번째 일꾼
    result = 0
    get_max_price(x, y, 0, 0, 0)
    priceA = result

    # 두 번째 일꾼
    priceB = 0
    j = y + m
    for i in range(x, n):
        j = j if i == x else 0
        while j < n - m + 1:
            result = 0
            get_max_price(i, j, 0, 0, 0)
            priceB = max(priceB, result)
            j += 1

    return priceA + priceB


t = int(input())

for tc in range(1, t + 1):
    n, m, c = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    max_price = 0

    # 슬라이딩 윈도우 방식으로 모두 돌리기
    for i in range(n):
        for j in range(n - m + 1):
            max_price = max(max_price, solve(i, j))

    print(f"#{tc} {max_price}")