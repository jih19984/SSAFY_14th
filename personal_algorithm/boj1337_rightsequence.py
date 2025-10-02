# 문제
"""
올바른 배열: 배열에 있는 원소 중 5개가 연속적인 것
* 배열에 중복되는 수는 없음

올바른 배열이 되기 위해 추가되어얄 원소의 최소 개수를 구하시오

<input>
첫째줄: 배열의 크기
이후에 배열의 원소가 나열됨
"""

# 풀이 방법
"""
4부터 시작했을 때 4, 5, 6, 7, 8 즉 맥스가 8이다.
즉, 각 원소를 하나씩 슬라이딩하며 5칸의 범위 내에 해당하는 원소가 몇개인지 구한 후 5에서 빼준다.
이 원소의 개수를 하나씩 비교하면서 min 갱신
"""

N = int(input())
lst = []

for _ in range(N):
    k = int(input())
    lst.append(k)

lst.sort()
best = 1000000000

for i in range(N):
    cnt = 5
    check_lst = lst[i:i+5]
    st = check_lst[0]
    tmp_lst = [i for i in range(st, st+5)]
    for ele in check_lst:
        if ele in tmp_lst:
            cnt -= 1

    best = min(best, cnt)

print(best)
