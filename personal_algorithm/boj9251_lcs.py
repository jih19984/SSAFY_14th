# 문제
"""
LCS: 최장 공통 부분 수열

두 수열이 주어졌을 때 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾으시오.

ACAYKP CAPCAK가 주어졌을 때
LCS는 ACAK가 된다.

메모리: 256mb
시간 0.1초

최대 1000글자
"""

# 풀이 방법
"""
각 문자열을 ord를 이용해 숫자로 변환 후 리스트에 저장
각 리스트의 값 중 1이상 공통적으로 가진 개수를 모두 더하면 최장 부분 수열이 된다.

-> 아 부분 집합이 아니라... 부분 수열이었음. 어쩐지 너무 쉬운 것 같더라.

이 문제는 LCS longest common subsequence 개념을 모르면 풀기 어렵다!

ACAYKP와 CAPCAK가 있다고 하자.
    C A P C A K Q
  0 0 0 0 0 0 0 0
A 0 0 1 1 1 1 1 1
C 0 1 1 1 2 2 2 2
A 0 1 2 2 2 3 3 3
Y 0 1 2 2 2 3 3 3
K 0 1 2 2 2 3 4 4
P 0 1 2 2 2 3 4 4
"""

import sys
input = sys.stdin.readline

# 두번째 문자열을 dp의 컬럼필드로 잡자
str1 = list(input().strip())
str2 = list(input().strip())

dp = [[0] * (len(str2)+1) for _ in range(len(str1)+1)]

for r in range(1, len(str1)+1):
    for c in range(1, len(str2)+1):
        if str1[r-1] == str2[c-1]:
            dp[r][c] = dp[r-1][c-1] + 1
        else:
            dp[r][c] = max(dp[r-1][c], dp[r][c-1])


print(dp[len(str1)][len(str2)])