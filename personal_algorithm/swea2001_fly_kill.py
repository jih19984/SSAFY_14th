# 문제
"""
NxN 배열이 있고, MxM 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.
죽은 파리의 개수를 구하라. (칸에 적혀있는 파리의 개수의 합을 구하면 됨)
5 <= N <= 15
2 <= M <= N
"""

# 풀이 방법
"""
1. 배열의 크기만큼 슬라이딩하면서 합 구하기
"""

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr_fly = [list(map(int, input().split())) for _ in range(N)]
    max_result = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            result = 0
            for a in range(M):
                for b in range(M):
                    result += arr_fly[i+a][j+b]
            max_result = max(result, max_result)

    print(f'#{tc} {max_result}')                