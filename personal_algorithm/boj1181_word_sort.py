# 문제
"""
알파벳 소문자 N개의 단어가 들어오면 다음 조건에 따라 정렬하시오.
1. 길이가 짧은 것부터
2. 길이가 같으면 사전 순으로

+ 중복된 단어는 하나만 남기기

1 <= N <= 20,000
주어진 문자열의 최대 길이 50
"""

# 풀이방법
"""
sort 정렬로 알파벳 순으로 정렬 후
다시 한 번 sort 정렬을 람다 표현식을 이용해 길이가 짧은 것부터 정렬되도록 조건문을 작성하면 된다.
그러나 소트를 2번하는 이 방식은 비효율적이다.

따라서 한 번에 2개의 조건을 적용하는 방법을 찾아본 결과 다음과 같다.
strs_lst.sort(key=lambda x: (len(x), x)) --> (우선순위1, 우선순위2)
위와 같이 적으면 len(x)를 기준으로 정렬 후 길이가 같은 경우 알파벳 순으로 정렬하게 된다.

"""

import sys
input = sys.stdin.readline

N = int(input())

# set로 중복 제거 후 다시 리스트로 변환
strs_lst = list(set([input().strip() for _ in range(N)]))

strs_lst.sort()
strs_lst.sort(key=lambda x:len(x))

for i in range(len(strs_lst)):
    print(strs_lst[i])