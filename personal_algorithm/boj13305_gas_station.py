# 문제
"""
왼쪽 -> 오른쪽으로 이동
인접한 두 도시 사이의 도로들은 서로 길이가 다를 수 있음

- 처음 출발할 때 기름 넣고 출발
- 기름통의 크기 무제한
- 1km/1L

각 도시에 있는 주소의 기름 가격과 도로의 길이를 입력 받아
이동하기 위한 최소 비용을 구하시오.
"""
import sys

input = sys.stdin.readline
N = int(input())

road_len = list(map(int, input().split()))
oil_pri = list(map(int, input().split()))

st_pri = oil_pri[0]
result = st_pri * road_len[0]

for i in range(1, N-1):
    if st_pri > oil_pri[i]:
        st_pri = oil_pri[i]

    result += st_pri * road_len[i]

print(result)