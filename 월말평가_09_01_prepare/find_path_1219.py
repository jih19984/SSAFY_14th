# 문제
"""
A -> B 로 가는 길이 존재하는가? 가능: 1, 불가능: 0
- 최대 2개의 갈림길이 존재
- A, B는 모두 0, 99로 고정
- 모든 길은 순서쌍으로 주어짐
- 거슬러 올라갈 수 없음

Constraints
- 출발점 0, 도착점 99
- 정점의 개수 98개
"""

# 풀이 방법
"""
문제에서 제시하는 방법
size[100]의 정적 배열 2개 선언
각 정점의 번호를 주소로 사용
"""

T = 10

for _ in range(T):
    t, n = map(int, input().split())
    paired_lst = list(map(int, input().split()))

    # 정적 배열 size:100 2개 생성
    arr1 = [-1] * 100
    arr2 = [-1] * 100

    # 정점 좌표 삽입
    for i in range(0, len(paired_lst), 2):
        st, en = paired_lst[i], paired_lst[i+1]

        if arr1[st] == -1:
            arr1[st] = en
        else:
            arr2[st] = en

    # DFS
    stack = []
    visited = [False] * 100

    # 출발점 0에서 시작
    stack.append(0)
    result = 0

    while stack:
        current = stack.pop()

        # 이미 방문한 곳 pass
        if visited[current]:
            continue
        visited[current] = True

        # 현재 위치가 도착점이면 성공
        if current == 99:
            result = 1
            break

        next_node1 = arr1[current]
        if next_node1 != -1 and not visited[next_node1]:
            stack.append(next_node1)

        next_node2 = arr2[current]
        if next_node2 != -1 and not visited[next_node2]:
            stack.append(next_node2)

    print(f"#{t} {result}")