# 문제
"""
N개의 수가 주어졌을 때 네가지 기본 통계값을 구하는 프로그램을 작성하시오.
산술평균
중앙값
최빈값
범위
"""

# 산술평균
def arithmetic_mean(lst):
    return sum(lst) / len(lst)

# 중앙값
def median(lst):
    lst.sort()
    return lst[len(lst)//2]

# 최빈값
# 여러 개 있을 경우 최빈값 중 두 번째로 작은 값을 출력
def mode(lst):
    dit = {}
    for i in lst:
         dit[i] = dit.get(i, 0) + 1

    # 최빈 빈도
    mode = max(dit.values())

    # 최빈 빈도 후보
    modes = [num for num, cnt in dit.items() if cnt == mode]

    if len(modes) >= 2:
        return modes[1]
    else:
        return modes[0]


# 범위
def partition(lst):
    return max(lst) - min(lst)

import sys
input = sys.stdin.readline
N = int(input())
lst = [int(input()) for _ in range(N)]
print(round(arithmetic_mean(lst)))
print(median(lst))
print(mode(lst))
print(partition(lst))