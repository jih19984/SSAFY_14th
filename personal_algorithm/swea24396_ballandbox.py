# 문제
"""
start: 06:22
end: 07:17
남은 공을 같은 색 상자에 넣어야 한다는 사실 망각

B개의 검은 공, B개의 검은 상자
W개의 흰 공, W개의 흰 상자

- 모든 상자가 정확히 한 개의 공을 담고있다.
- 검은 상자에 검은 공 X점, 흰 상자에 흰 공 Y점, 이외 Z점

-> 모든 상자의 점수 최대합은?
"""


import sys
input = sys.stdin.readline

T = int(input())

for _ in range(1, T+1):
    B, W, X, Y, Z = map(int, input().split())
    min_cnt = min(B, W)
    max_cnt = max(B, W)
    cnt_diff = max_cnt - min_cnt

    score1 = B * X + W * Y

    score2 = min_cnt * 2 * Z
    
    if cnt_diff != 0:
        if max_cnt == B:
            remains = cnt_diff * X
        else:
            remains = cnt_diff * Y
    else:
        remains = 0

    score2 += remains

    result = max(score1, score2)
    print(result)