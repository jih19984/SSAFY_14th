# 문제
"""
- 처음 주사위를 던지면 나온 숫자대로 1에서 6번 칸에 도착한다.
- 이후에는 나온 숫자만큼 현재 칸 번호에 더한 칸으로 이동한다.
- 도착한 칸에 화살표가 있으면, 바로 화살표가 가리키는 칸으로 이동한다.
- 마지막 칸 N 이상의 숫자에 도달하거나, 정해진 횟수 K만큼 주사위를 다 던지면 게임은 끝난다.

<Input>
첫 줄에 테스트케이스의 개수 T
각 테스트 케이스마다 첫 줄에 N, K, E가 빈칸으로 구분되어 주어짐.
다음 줄부터 E개의 줄에 걸쳐 화살표의 출발 도착 칸 번호가 주어진다.

<Output>
주사위를 K번 이내로 던질 때 도착할 수 있는 최대 번호
N보다 큰 숫자에 도착하는 경우는 N으로 표시한다.
"""

def game(now, do_dice):
    if now < N and board[now]:
        now = board[now]

    if now >= N:    # N이 큰지부터 확인해야 함
        end.append(20)
        return
    if do_dice == K:
        end.append(now)
        return

    for i in range(1, 7):   # 주사위 굴리기
        game(now + i, do_dice + 1)


T = int(input())
for tc in range(T):
    N, K, E = map(int, input().split())

    board = [0 for _ in range(N + 1)]

    for _ in range(E):
        n_from, n_to = map(int, input().split())
        board[n_from] = n_to

    end = []
    game(0, 0)
    # print(end)
    print(max(end))