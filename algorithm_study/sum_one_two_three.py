# 문제
"""
정수 n을 1, 2, 3의 합으로 나타낼 수 있는 경우의 수를 구하시오.
"""

# 풀이 방법
"""
-> 1 또는 2 또는 3을 더하는 dfs 형태의 함수를 만든다.

- 종료 조건: 정수 n이 될 때 
1. 종료 조건에 도달할 수 있으면 개수를 한 개 더해주고
2. 종료 조건에 도달할 수 없으면 return 0

- 맨 마지막 분기에 도달했을 때 return되면서 return 값만을 가져오기 위해
ways 변수에 더해준다. 단 ways_변수는 뒤에 있는 분기의 영향을 받으면 안되기 때문ㅇ
매번 0으로 초기화 시킨다.
"""
import sys
input = sys.stdin.readline

def dfs(total):
    if total == N: # 종료 조건
        return 1
    if total > N: # 값을 초과하면 0
        return 0 
    
    ways = 0 # 마지막 종점에서 윗 분기로 올라올 때 ways = 0이 되어야 맨끝점의 ways 값만 가지고 올 수 있음.
    for num in (1, 2, 3):
        ways += dfs(total + num)
    return ways

T = int(input())

for _ in range(T):
    N = int(input())
    print(dfs(0))