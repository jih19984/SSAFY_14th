# 문제
"""
2개의 숫자 N, M이 주어질 때 N의 M 제곱 값을 구하는 프로그램을 재귀호출을 이용해 구현하시오.
총 10개의 테스트 케이스가 주어진다.
"""

def power(n, m):
    # m이 0이면 1 반환
    if m == 0:
        return 1

    return n * power(n, m - 1)

for _ in range(10):
    tc = int(input())
    n, m = map(int, input().split())
    result = power(n, m)
    print(f"#{tc} {result}")