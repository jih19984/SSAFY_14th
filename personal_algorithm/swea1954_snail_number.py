# 문제
"""
빙글빙글 돌아가는 숫자판이 있다.
숫자판의 크기 N이 주어질 때 숫자판을 출력하시오.
"""
from collections import deque

T = int(input())

for tc in range(1, T+1):
    print(f"#{tc}")
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    """
    0: 초기, 1: 우, 2: 하, 3: 좌, 4: 상
    """
    dir = 0
    arr_num = 0
    r, c = 0, 0

    while arr_num < N**2:
        arr_num += 1

        if dir == 0:
            arr[r][c] = arr_num
            dir = 1
            
        elif dir == 1:
            if c+1 < N and arr[r][c+1] == 0:
                c += 1
                arr[r][c] = arr_num
            else:
                r += 1
                arr[r][c] = arr_num
                dir = 2
        
        elif dir == 2:
            if r+1 < N and arr[r+1][c] == 0:
                r += 1
                arr[r][c] = arr_num
            else:
                c -= 1
                arr[r][c] = arr_num
                dir = 3

        elif dir == 3:
            if c-1 >= 0 and arr[r][c-1] == 0:
                c -= 1
                arr[r][c] = arr_num
            else:
                r -= 1
                arr[r][c] = arr_num
                dir = 4

        elif dir == 4:
            if r-1 >= 0 and arr[r-1][c] == 0:
                r -= 1
                arr[r][c] = arr_num
            else:
                c += 1
                arr[r][c] = arr_num
                dir = 1

    for row in arr:
        print(*row)




