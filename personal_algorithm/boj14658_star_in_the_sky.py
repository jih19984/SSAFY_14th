# 문제
"""
L*L 크기의 트램펄린을 배치하여 떨어지는 K개의 별똥별을 최대한 많이 막아내는 문제.
별똥별의 위치는 (x, y) 좌표로 주어지며, 트램펄린은 회전할 수 없다.
지구에 빗발치는(막지 못한) 별똥별의 최소 개수를 구해야 한다.
"""

# 풀이 방법
"""
트램펄린의 경계선에 별똥별이 걸쳐 있을 때 최적의 해를 찾을 수 있다는 점을 이용한다.
모든 별의 x좌표와 y좌표들을 각각 후보로 하여, 이들의 조합 (star[i].x, star[j].y)를 
트램펄린의 왼쪽 위 모서리로 가정하고 완전 탐색한다.
"""

import sys
input = sys.stdin.readline

def solve():
    # 입력 받기
    # 첫째 줄: N, M, L, K
    N, M, L, K = map(int, input().split())

    stars = []
    # 이후 K개의 줄: 별똥별 좌표
    for _ in range(K):
        # input()은 readline()이므로 한 줄씩 읽습니다.
        line = input().split()
        stars.append((int(line[0]), int(line[1])))
        
    max_deflected = 0
    
    # 두 별의 좌표를 조합하여 트램펄린의 좌상단(모서리) 후보를 설정
    # (i번째 별의 x좌표, j번째 별의 y좌표)가 트램펄린의 시작점이라고 가정
    for i in range(K):
        for j in range(K):
            test_x = stars[i][0]
            test_y = stars[j][1]
            
            # 현재 배치된 트램펄린 안에 들어오는 별의 개수 카운트
            count = 0
            for k in range(K):
                sx, sy = stars[k]
                if test_x <= sx <= test_x + L and test_y <= sy <= test_y + L:
                    count += 1
            
            max_deflected = max(max_deflected, count)

    # 정답 = 전체 별 개수 - 최대로 막아낸 별 개수
    print(K - max_deflected)

solve()