# 문제
"""
N줄에 0 이상 9이하의 숫자가 세 개씩 적혀있다.

- 먼저 처음에 적혀 있는 세 개의 숫자 중 하나를 골라 시작한다.
- 그 다음 바로 아래의 수로 넘어가거나 그 수의 인접한 수로 넘어갈 수 있다.

-> 숫자표가 주어졌을 때 얻을 수 있는 최대점수, 최소점수를 구하시오.

3
1 2 3
4 5 6
4 9 0

N은 10만 이하의 자연수
"""

# 풀이 방법
"""
최소와 최대를 저장하는 
dp 배열을 2개 만들자.

어떻게 값을 선택할 것인가?
최대인 경우
첫 줄은 기본값 넣어주기
둘째 줄부터
max(1->4, 2->4), max(2->5, 1->5, 3->5), max(2->6, 3->6)

즉 범위를 벗어나지 않는 선에서 좌우대각선과 위의 값을 비교해 큰 값을 해당 dp 배열에 값을 저장

-> 왜 시간초과가 날까?
메모리자체가 60만개가 되며 이는 캐시 초과로 이어질 수 있다.
애초에 dp 배열이 끝에줄만 필요하므로 크기를 크게 만들 필요가 없다. (열이 3개로 고정))
"""

import sys

input = sys.stdin.readline

N = int(input())

# 문제에서 메모리 제한이 4메가이기 때문에 아래와 같은 방법은 안됨.
# arrs = [list(map(int, input().split())) for _ in range(N)]
# dr = [-1, -1, -1] 
dp_max = [0] * 3
dp_min = [100001] * 3

for r in range(N):
    arrs = list(map(int, input().split()))
    if r == 0:
        dp_max[0], dp_max[1], dp_max[2] = arrs[0], arrs[1], arrs[2]
        dp_min[0], dp_min[1], dp_min[2] = arrs[0], arrs[1], arrs[2]

    else:
        tmp_0, tmp_1, tmp_2 = dp_max[:][0], dp_max[:][1], dp_max[:][2]
        tmp_3, tmp_4, tmp_5 = dp_min[:][0], dp_min[:][1], dp_min[:][2]

        dp_max[0] = max(tmp_0+arrs[0], tmp_1+arrs[0])
        dp_max[1] = max(tmp_0+arrs[1], tmp_1+arrs[1], tmp_2+arrs[1])
        dp_max[2] = max(tmp_1+arrs[2], tmp_2+arrs[2])
        dp_min[0] = min(tmp_3+arrs[0], tmp_4+arrs[0])
        dp_min[1] = min(tmp_3+arrs[1], tmp_4+arrs[1], tmp_5+arrs[1])
        dp_min[2] = min(tmp_4+arrs[2], tmp_5+arrs[2])

print(f"{max(dp_max)} {min(dp_min)}")