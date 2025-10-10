# 문제
"""
R x C 격자판
- 폭탄이 있는 칸은 3초가 지난 후 폭발
- 폭탄은 현재칸과 인접한 4칸을 모두 파괴
- 인접한 칸에 폭탄이 추가로 있다면 해당 폭탄은 폭발없이 파괴된다.
- 봄버맨은 폭탄에 면역이 있음.

봄버맨의 이동 조건
- 가장 처음에 봄버맨은 일부 칸에 폭탄을 설치해 놓는다 : 0초
- 1초 동안 봄버맨은 아무것도 안함: 1초
- 다음 1초 동안 폭탄이 설치되지 않은 모든 칸에 폭탄 설치 : 2초 ...1
- 1초가 지난 후에 3초 전에 설치된 폭탄이 모두 폭발: 3초 ...2
- 1번과 2번을 반복

폭탄을 설치해놓은 초기 상태가 주어졌을 때, N초가 흐른 후 격자판 상태를 구하자

"""

# 풀이 방법
"""
<input>
...
.O. 0초
...

OOO
OOO 1초, 2초
OOO

O.O
... 3초 (0초에 설치된 폭탄 파괴)
O.O

각 좌표에 sec를 값으로 가지는 2차원 배열 생성
000
030 초기 설정
000

000
020 모든 칸의 초를 -1
000

333
313 0인 칸에 폭탄 설치 후 폭탄이 설치된 칸의 sec-1
333

202
000 1인 칸과 인접 칸의 초를 모두 0으로 변환
202 

"""

import sys

input = sys.stdin.readline

def find_st_bomb() -> None: 
    for r in range(R):
        for c in range(C):
            if arr[r][c] == 'O':
                sec_arr[r][c] = 3 # 초기 bomb 위치 sec 3초로 설정
                
def fill_bomb() -> None:
    for r in range(R):
        for c in range(C):
            if arr[r][c] == '.':
                arr[r][c] = 'O' # 빈 칸에 폭탄 채우기
                sec_arr[r][c] = 3
            else:
                sec_arr[r][c] -= 1

# 폭탄은 모두 동시에 터져야 한다!!
# 따라서 sec = 1인 좌표를 한 번에 모아서 터뜨린다.
# 현재 위치의 폭탄은 터뜨려도 되지만 주변의 폭탄은 모아서 터뜨릴 것!
# 한 번에 터뜨릴 좌표 리스트 all_bomb 생성
def pop_bomb() -> None:
    for r in range(R):
        for c in range(C):
            if sec_arr[r][c] == 1:
                sec_arr[r][c] = 0
                arr[r][c] = '.'
                # 터지는 폭탄이라면
                # 주변 밑 현재 위치의 arr, sec_arr 재조정
                for rr, cc in zip(dr, dc):
                    nr = r + rr
                    nc = c + cc
                    # 폭탄이 터지면 주변 폭탄 전부 없애고 sec 초기화
                    if 0 <= nr < R and 0 <= nc < C:
                        if arr[nr][nc] == 'O':
                            arr[nr][nc] = '.'
                            all_bomb.append((nr, nc))
                            
    for bomb_loc in all_bomb:
        r, c = bomb_loc
        sec_arr[r][c] == 0
                                
    for r in range(R):
        for c in range(C):                        
            # 폭탄을 다 터뜨리고 난뒤 남은 폭탄이 있는 위치의 sec-1
            if arr[r][c] == 'O':
                sec_arr[r][c] -= 1
                
R, C, N = map(int, input().split())

arr = [list(input().strip()) for _ in range(R)]
sec_arr = [[0] * C for _ in range(R)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
all_bomb = []

find_st_bomb() # 좌표 설정 (0초)

# N초가 될 때까지 while문 반복
sec = 1
"""
0초에 설치한 거는 3초
2초에 설치한 거는 5초
4초에 설치한 거는 7초
"""

while sec <= N:
    if sec == 1:
        sec += 1
        for r in range(R):
            for c in range(C):                        
                if arr[r][c] == 'O':
                    sec_arr[r][c] -= 1           
        continue
    
    if sec == 2:
        fill_bomb()
        sec += 1

        continue
    
    if sec == 3:
        pop_bomb()
        sec += 1

        continue
    
    if sec >= 4:
        if sec % 2 == 0:
            fill_bomb()
        else:
            pop_bomb()
    
    sec += 1
    
for ele in arr:
    print(''.join(ele))


