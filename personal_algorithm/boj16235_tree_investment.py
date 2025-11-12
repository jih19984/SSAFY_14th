# 문제
"""
start 01:00
end: 02:00

NxN 크기의 땅을 구매

- r과 c는 1부터 시작
- M개의 나무를 구매해 땅에 심었다
- 1x1 크기의 칸에 여러 개의 나무가 심어져 있을 수 있음

봄 
-> 양분 증가: 나이, 나이 +1
-> 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹음.
-> 만약 양분이 부족하다면 양분을 먹을 수 없는 나무는 즉시 죽음

여름
-> 봄에 죽은 나무가 양분으로 변환
-> 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가 (소수점 버림)

가을
-> 번식하는 나무는 나이가 5의 배수
-> 인접한 8개의 칸에 나이가 1인 나무가 생김

겨울
-> 땅에 양분 추가. 각 칸에 추가되는 양분의 양 A[r][c]. 입력으로 주어진다.
"""

# 풀이
"""
<input>
- 첫째 줄에 N, M, K
- N개의 줄에 A배열의 값이 주어짐
- 상도가 심은 나무의 정보를 나타내는 정수가 주어짐. (x, y, age)

<restriction>
1 ≤ N ≤ 10
1 ≤ M ≤ N^2
1 ≤ K ≤ 1,000
1 ≤ A[r][c] ≤ 100
1 ≤ 입력으로 주어지는 나무의 나이 ≤ 10
입력으로 주어지는 나무의 위치는 모두 서로 다름

<output>
- K년이 지난 후 살아남은 나무의 수를 출력하시오.

문제를 보면 가장 작은 나이를 기준으로 빼낸다고 적혀 있어서
우선순위 큐인 heapq를 사용 (힙큐는 기본적으로 최소힙 구조)
"""

import sys
import heapq
from heapq import heappush, heappop
import time

start = time.time()
input = sys.stdin.readline

N, M, K = map(int, input().split())

# 초기 양분
arr = [[5] * N for _ in range(N)]

# 양분 추가 배열
add_arr = [list(map(int, input().split())) for _ in range(N)]    
heap = []

# 8방향
dir_r = [-1, -1, -1, 0, 0, 1, 1, 1]
dir_c = [-1, 0, 1, -1, 1, -1, 0, 1]

# queue에 나무의 위치와 age 정보를 튜플로 묶어서 추가
for _ in range(M):
    r, c, age = map(int, input().split())
    # 문제에서 1,1부터 시작하기 때문에 -1을 하여 푸쉬
    heapq.heappush(heap, [age, r-1, c-1])

for _ in range(K):
    # 봄
    # 양분은 나이가 어린 나무부터 증가
    # 양분이 부족해서 먹을 수 없는 나무는 즉시 죽음
    # 1. 나이만큼 양분 증가
    # 2. 나이 + 1
    new_heap = []
    dead_trees = []

    while heap:
        age, r, c = heapq.heappop(heap)

        if arr[r][c] >= age:
            arr[r][c] -= age
            heapq.heappush(new_heap, [age+1, r, c])
        else:
            dead_trees.append([age, r, c])

    heap = new_heap

    # 여름
    # 봄에 죽은 나무가 양분으로 변환
    # 죽은 나무마다 2로 나눈 값이 나무가 있던 칸에 양분으로 추가됨.

    for age, r, c in dead_trees:
        arr[r][c] += age//2

    # 가을
    breeding = []  # 번식할 나무 따로 모음
    for age, r, c in heap:
        if age % 5 == 0:
            breeding.append((r, c))

    for r, c in breeding:
        for dr, dc in zip(dir_r, dir_c):
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                heapq.heappush(heap, [1, nr, nc])

            
    # 겨울
    # 각 칸에 양분 추가
    for r in range(N):
        for c in range(N):
            arr[r][c] += add_arr[r][c]
        
print(len(heap))        
end = time.time()

print(f"{end-start}")


