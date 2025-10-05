# 문제
"""
들어보지 못한 사람과 보지 못한 사람 명단이 주어질 때 듣도 보도 못한 사람의 명단을 구하시오.
N개의 줄에 걸쳐 들어보지 못한 사람과 M개의 줄에 걸쳐 보지 못한 사람이 주어진다.

각 명단에는 중복된 이름이 없다.
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
set_hear = set()
set_see = set()

for _ in range(N):
    hear = input().strip()
    set_hear.add(hear)

for _ in range(M):
    see = input().strip()
    set_see.add(see)

set_common = set_hear & set_see

print(len(set_common))
list_common = list(set_common)
list_common.sort(key=lambda x:x)
for i in range(len(set_common)):
    print(list_common[i])
