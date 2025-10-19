# 문제
"""
돈을 많이 번 민기는 지하 9999억 층에서 지상 9999억 층에 이르는 건물을 건설
4가 들어가는 모든 층을 건너뛰어 건물을 설계하였다.

- 건물에 0층 존재하지 않음.

은비는 이 건물의 청소부인데,
A층에서 B층으로 올라가려면 몇 층을 올라가야 하는가?
"""

# 풀이 방법
"""
규칙을 찾아야 할 것 같은 느낌?
4의 개수를 어떻게 구할 것인가?
1자리 -> 1가지
2자리 -> 십의자리(1~3, 5~9, 1 * 8가지) + 십의자리(4, 10가지) = 18가지
3자리 -> 18가지 * 8 + 백의자리(4, 100가지) = 244가지
4자리 -> 위와 같은 방식으로 연산

1자리 -> dp[1] = 1
2자리 -> dp[2] = dp[1] * 8 + 10^1
3자리 -> dp[3] = dp[2] * 8 + 10^2
k자리 -> dp[k] = dp[k] * 8 + 10^(k-1)
"""
# GPT 풀이
def count_with4_upto(N: int) -> int:
    """0 ~ N 사이 '4가 포함된 수' 개수를 정확히 계산 (직접 캐시 버전)"""
    if N < 0:
        return 0
    s = str(N)
    cache = {}  # 직접 캐시(메모이제이션) 딕셔너리

    def dp(pos: int, tight: bool, has4: bool) -> int:
        key = (pos, tight, has4)
        if key in cache:
            return cache[key]

        if pos == len(s):
            return 1 if has4 else 0

        limit = int(s[pos]) if tight else 9
        total = 0
        for d in range(0, limit + 1):
            ntight = tight and (d == limit)
            nhas4 = has4 or (d == 4)
            total += dp(pos + 1, ntight, nhas4)

        cache[key] = total
        return total

    return dp(0, True, False)


def count_without4(N: int) -> int:
    """1 ~ N 사이 '4가 없는 수' 개수"""
    if N <= 0:
        return 0
    return N - count_with4_upto(N)


def climb(A: int, B: int) -> int:
    """A층에서 B층까지 실제 존재하는 층 수 계산"""
    if A * B > 0:  # 같은 부호
        return abs(count_without4(B) - count_without4(A))
    else:  # 부호 다름 (0층 없음)
        return count_without4(abs(A)) + count_without4(B) - 1


# ---------------------------
# 메인 실행부
# ---------------------------
T = int(input())
for t in range(1, T + 1):
    A, B = map(int, input().split())
    print(f"#{t} {climb(A, B)}")
