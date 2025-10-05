# 문제
"""
세준이는 시험 점수를 조작하기로 했다.
1. 자기 점수 중에 최댓값을 고른다. -> 최댓값: M
2. 모든 점수를 점수/M*100으로 수정
"""

import sys
input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))
max_score = max(lst)

for i in range(N):
    lst[i] = lst[i] / max_score * 100

print(sum(lst)/N)