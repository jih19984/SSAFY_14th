# 문제
"""
1번부터 N번까지의 번호가 부여된 N(1<=N<=100)개의 물건과 최대 K(1<=K<=100) 부피만큼 넣을 수 있는 가방이 있다.
1번 물건부터 N번 물건 각각은 부피 V와 가치 C를 가지고 있다. (1<= V, C <= 100)
민수는 물건들 중 몇 개를 선택하여 가방에 넣어 그 가치의 합을 최대화 하려고 한다.
단, 선택된 물건들의 부피 합이 K 이하여야 한다.

민수가 가방에 담을 수 있는 최대 가치를 계산하자.
"""

# 풀이 방법
"""
4 5

1 2
2 3
3 2
4 4
"""

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    items = [(0, 0)]

    for _ in range(N):
        V, C = map(int, input().split())
        items.append((V, C))

    dp = [[0] * (K+1) for _ in range(N+1)]

    for i in range(1, N+1):
        V, C = items[i]
        for v in range(K+1):
            if V > v:
                dp[i][v] = dp[i-1][v]
            else:
                dp[i][v] = max(dp[i-1][v], dp[i-1][v-V] + C)
    
    print(f"#{tc} {dp[N][K]}")

