# 문제
"""
start 15:03
end 15:25
RC카의 이동거리를 계산하려고 한다.

<command>
0: 현재 속도 유지
1: 가속
2: 감속

- 가속 또는 감속의 경우 가속도 값이 추가로 주어짐
- RC카의 초기 속도 0

입력으로 주어진 N개의 커맨드를 모두 수행했을 때, N초 동안 이동한 거리를 계산하는 프로그램을 작성하라.

<제약사항>
- 2 <= N <= 30
- 가속도 값 1m/s^2 or 2m/s^2
- 현재 속도보다 감속할 속도가 더 클 경우, 속도가 0m/s
"""

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    now_speed = 0
    now_distance = 0

    for _ in range(N):
        command_accels = list(map(int, input().split()))
        if len(command_accels) > 1:
            command, accel = command_accels[0], command_accels[1]
        else:
            command = 0

        # 초기 속도 유지
        if command == 0:
            pass
        # 가속
        elif command == 1:
            now_speed += accel
        # 감속
        elif command == 2:
            now_speed -= accel
            if now_speed < 0:
                now_speed = 0

        now_distance += now_speed

    print(f"#{tc} {now_distance}")