# 문제
"""
start: 20:55
end:

축구를 하기 위해 모인 사람: N명
스타트팀과 링크팀을 N/2명으로 나눠야 한다.

능력치 Sij
-> i번과 j번 사람이 같은 팀에 속했을 때,
   팀에 더해지는 능력치

- Sij, Sji는 다를 수 있음
- i번 사람과 j번 사람이 같은 팀에 속했을 때,
  더해지는 능력치는 두 수의 합

축구를 재밌게 하기 위해 스타트팀의 능력치와
링크 팀의 능력치 차이를 최소로 하고자 한다.

6/2 3 -> 4, 5, 2 / 1, 3, 6 / 
(4,5), (5,4), (2,4), (4,2), (2,5), (5,2)

이 문제를 어떻게 풀 것인가?
조합을 써서 풀어야 한다!
조합을 itertools를 쓰지말고, 함수를 만들어서 구현해보자!

1. 숫자를 N/2개를 뽑고
2. 뽑은 값의 arr합과 안뽑은 값의 arr합의 차이를 구한다.
"""

import sys
input = sys.stdin.readline

def solve():
    N = int(input().strip())
    S = [list(map(int, input().split())) for _ in range(N)]
    P = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            P[i][j] = P[j][i] = S[i][j] + S[j][i]

    players = range(N)
    best = float('inf')
    result1 = []
    result2 = []
    result3 = []
    tmp = []

    def combinations1(st, cnt):
        if cnt == N//2:
            result1.append(tmp.copy())
            return
        
        for idx in range(st, N):
                tmp.append(idx)
                combinations1(idx+1, cnt+1)
                tmp.pop()

    def combinations2(st, cnt, arr):
        if cnt == 2:
            result2.append(tmp.copy())
            return
        
        for idx in range(st, len(arr)):
            tmp.append(arr[idx])
            combinations2(idx+1, cnt+1, arr)
            tmp.pop()
    
    def combinations3(st, cnt, arr):
        if cnt == 2:
            result3.append(tmp.copy())
            return
        
        for idx in range(st, len(arr)):
            tmp.append(arr[idx])
            combinations3(idx+1, cnt+1, arr)
            tmp.pop()

    combinations1(0, 0)

    for teamA in result1:
        if 0 not in teamA:
            continue

        teamB = [p for p in players if p not in teamA]
        result2.clear()
        sumA = 0

        combinations2(0, 0, teamA)
        for res in result2:
            i, j = res[0], res[1]
            sumA += P[i][j]

        result3.clear()
        sumB = 0

        combinations3(0, 0, teamB)
        for res in result3:
            i, j = res[0], res[1]
            sumB += P[i][j]

        best = min(best, abs(sumA - sumB))
        if best == 0:
            break
    
    return best

print(solve())