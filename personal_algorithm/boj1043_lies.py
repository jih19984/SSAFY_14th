# 문제
"""
- 사람의 수 N, 파티의 수 M 
- 이야기의 진실을 아는 사람의 수, 번호(1 ~ N)
    -> 진실을 아는 사람의 수가 먼저 주어지고 그 개수만큼 사람들의 번호가 주어진다
- 각 파티마다 오는 사람의 수와 번호가 같은 방식으로 주어짐

1 <= N, M <= 50
* 진실을 아는 사람의 수 0이상 50 이하의 정수
* 각 파티마다 오는 사람의 수는 1 이상 50 이하의 정수

-> 모든 파티에 참가할 때, 거짓말을 들키지 않고 과장된 이야기를 할 수 있는 파티 개수의 최댓값을 구하시오.
"""

# 풀이 방법
"""
<example 1>

3 4
1 3
1 1
1 2
2 1 2
3 1 2 3
3 1 2 4

3번은 거짓말을 알고 있다.
{1} 안됨
{2} 안됨
{1,2} 안됨
{1,2,3} 사실대로 무조건 말해야한다 -> 1,2,3은 사실을 알고 있음.

따라서 거짓말을 할 수 있는 파티 0

<example 2>

10 9
4 1 2 3 4
2 1 5 사실
2 2 6 사실
1 7 거짓말
1 8 거짓말
2 7 8 같이 있으므로 안됨
1 9 거짓말
1 10 거짓말
2 3 10 사실
1 4 사실

7, 8, {7,9}, {7,8}, {9,10}, {10,11}
어떻게 거짓말 할 수 있는 파티의 개수 최대를 구해야할까?
각 집합에서 각 원소들이 포함된 개수를 모두 세어본다
이후 가장 적은 원소를 포함한 집합먼저 거짓말을 한다고 생각한다.

------------------------------------------------------------------
그렇다면 어떻게 문제를 풀어야할까?

1. 거짓말을 알고 있는 파티들을 먼저 조사한다!
2. 이후 해당 파티에 같이 있는 멤버들을 진실을 아는 집합에 추가
3. 이후 거짓말을 아는 집합의 원소가 다른 집합에 하나라도 있으면 해당 집합 거짓말 불가
4. 거짓말을 아는 집합과 하나도 겹치지 않는 집합은 파티의 수 +1
    그리고 해당 집합은 거짓말을 한 집합입므로 이 집합 역시 다른 집합의 원소와 겹친다면 거짓말 불가
"""

import sys
input = sys.stdin.readline

# 사람의 수, 파티의 수
N, M = map(int, input().split())

# 진실을 아는 사람의 수, 해당 사람들의 번호
know_fact_input = list(map(int, input().split()))
if know_fact_input[0] == 0:
    know_fact = []
else:
    know_fact = know_fact_input[1:]

# 각 파티 별 리스트 저장   
party_people_num_lst = []
for _ in range(M):
    party_lst = list(map(int, input().split()))
    party_people_num_lst.append(party_lst[1:])

# Union-Find 구현
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    px, py = find(parent, x), find(parent, y)
    if px == py:
        return
    if rank[px] < rank[py]:
        parent[px] = py
    elif rank[px] > rank[py]:
        parent[py] = px
    else:
        parent[py] = px
        rank[px] += 1

# Union-Find 초기화
parent = [i for i in range(N + 1)]
rank = [0] * (N + 1)

# 같은 파티에 참석하는 사람들을 union
for party in party_people_num_lst:
    for i in range(len(party) - 1):
        union(parent, rank, party[i], party[i + 1])

# 진실을 아는 사람들의 루트를 찾기
if len(know_fact) == 0:
    # 진실을 아는 사람이 없으면 모든 파티에서 거짓말 가능
    print(M)
else:
    truth_roots = set()
    for person in know_fact:
        truth_roots.add(find(parent, person))
    
    # 각 파티를 확인해서 거짓말 가능한 파티 개수 세기
    lie_count = 0
    for party in party_people_num_lst:
        can_lie = True
        for person in party:
            if find(parent, person) in truth_roots:
                can_lie = False
                break
        if can_lie:
            lie_count += 1
    
    print(lie_count) 
    
    
    