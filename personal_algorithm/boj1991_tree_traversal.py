# 문제
"""
이진 트리를 입력 받아
전위 순회, 중위 순회, 후위 순회한 결과를 출력하는 프로그램을 작성하시오.
"""

import sys
input = sys.stdin.readline

N = int(input())
tree = {}

for _ in range(N):
    node, left, right = input().split()
    tree[node] = (None if left == '.' else left, None if right == '.' else right)

pre = []
order = []
post = []

def preorder(node):
    if node is None:
        return

    pre.append(node)
    preorder(tree[node][0])
    preorder(tree[node][1])

def inorder(node):
    if node is None:
        return

    inorder(tree[node][0])
    order.append(node)
    inorder(tree[node][1])

def postorder(node):
    if node is None:
        return

    postorder(tree[node][0])
    postorder(tree[node][1])
    post.append(node)

preorder('A')
inorder('A')
postorder('A')

print(''.join(pre))
print(''.join(order))
print(''.join(post))