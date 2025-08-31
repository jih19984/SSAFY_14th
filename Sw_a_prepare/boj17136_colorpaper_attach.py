import sys

# 문제
"""
- 10x10 보드의 1을 1~5 크기의 색종이(각 5장)로 모두 덮기
- 불가능하면 -1, 가능하면 최소 사용 장수
"""

# 풀이 방법
"""
색종이를 넣을 수 있다면 사이즈가 큰 것부터 채워넣고,
각각의 함수를 정의하고 재귀와 가지치기를 통해 백트래킹을 구현한다,

can_place: 사이즈 s의 색종이를 놓을 수 있는지 확인하는 함수
set_square: r,c의 좌표로부터 s사이즈만큼 값을 0 or 1로 변환
next_one: 1이 있는 좌표를 찾아주는 함수 ex) 85를 return 한 후 85 / 10 -> (8, 5)
dfs: 가지치기 + 종료조건 + 탐색(모든 선택지 시도)
"""

# 입력: 10줄을 읽어 10x10 보드 구성
input = sys.stdin.readline()
board = [list(map(int, input.split())) for _ in range(10)]

# 각 크기(1~5)별 남은 색종이 수. 인덱스 0은 미사용.
remain = [0, 5, 5, 5, 5, 5]

# 현재까지 찾은 최소 사용 장수(초기값: 무한대)
best = [float("inf")]  # 굳이 리스트로 감싸지 않고, float("inf")로 무한대의 실수 생성 후 함수 내부에서 global 선언해줘도 okay. 파이썬에서 실수는 지역변수로 처리됨.


def can_place(r: int, c: int, s: int) -> bool:
    #(r, c)를 좌상단으로 하는 s×s 색종이를 놓을 수 있나?
    if r + s > 10 or c + s > 10:
        return False
    for i in range(r, r + s):
        for j in range(c, c + s):
            if board[i][j] != 1:
                return False
    return True


def set_square(r: int, c: int, s: int, val: int) -> None:
    #(r, c) ~ (r+s-1, c+s-1) 구간을 val(0 or 1)로 설정.
    for i in range(r, r + s):
        for j in range(c, c + s):
            board[i][j] = val


def next_one(start_idx: int) -> int:
    for idx in range(start_idx, 100):
        r, c = divmod(idx, 10)
        if board[r][c] == 1:
            return idx
    return 100


def dfs(used: int, start_idx: int) -> None:
    # 가지치기: 이미 최적해 이상이면 중단
    if used >= best[0]:
        return

    idx = next_one(start_idx) # 검사할 시작 인덱스 찾기
    if idx == 100: # 종료 조건
        best[0] = min(best[0], used)
        return

    r, c = divmod(idx, 10)

    # 큰 색종이부터 시도 (5 → 1)
    for s in range(5, 0, -1):
        if remain[s] == 0:
            continue
        if can_place(r, c, s):
            remain[s] -= 1
            set_square(r, c, s, 0)

            # 같은 idx부터 다시 스캔(덮은 영역은 0이므로 자동으로 다음 1로 감)
            dfs(used + 1, idx)

            # 복구
            set_square(r, c, s, 1)
            remain[s] += 1


# 탐색 시작 + 결과 출력
dfs(0, 0)
print(-1 if best[0] == float("inf") else best[0])


