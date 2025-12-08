# 문제
"""
start 15:50
end 16:15
1. 알파벳 소문자로 이루어진 문자열 W가 주어짐.
2. 양의 정수 K
3. 어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이를 구한다.
4. 어떤 문자를 정확히 K개를 포함하고, 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이를 구한다.

위와 같은 방식으로 게임을 T회 진행

<입력>
T

T번 주어진다.
W
K

<출력>
T개의 줄 동안 문자열 게임의 3, 4번에서 구한 연속된 문자열의 길이를 출력
만약 만족하는 연속 문자열이 없으면 -1 출력
"""

""" 1. 입력 정의 """
import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())

""" 2. 입력받은 문자열에서 각 문자 요소들의 인덱스를 딕셔너리에 저장"""
for _ in range(T):
    W = input().strip()
    K = int(input())

    if K == 1:
        print("1 1")
        continue

    char_idxs = defaultdict(list)
    
    for idx, char in enumerate(W):
        char_idxs[char].append(idx)

    min_len = float('inf')
    max_len = -1

    """ 3. 슬라이딩 윈도우 공식 이용 """
    for char, idxs in char_idxs.items():
        if len(idxs) < K:
            continue
    
        for i in range(len(idxs) - K + 1):
            length = idxs[i+K-1] - idxs[i] + 1
            min_len = min(min_len, length)
            max_len = max(max_len, length)
            
    """ 4. 만약에 max_len이 초기값 그대로라면, -1 출력. """
    if max_len == -1:
        print(-1)
    else:
        print(min_len, max_len)