import sys
input = sys.stdin.readline

def update(idx, val):
    while idx <= N + M:
        tree[idx] += val
        idx += (idx & -idx)

def query(idx):
    result = 0
    while idx > 0:
        result += tree[idx]
        idx -= (idx & -idx)
    return result


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    movie_idx = [0] * (N + 1)
    tree = [0] * (N + M + 1)

    for i in range(1, N + 1):
        movie_idx[i] = M + i
        update(movie_idx[i], 1)

    select_list = list(map(int, input().split()))
    result = []

    for i in range(M):
        select = select_list[i]
        selectIdx = movie_idx[select]

        result.append(query(selectIdx - 1))

        update(selectIdx, -1)
        movie_idx[select] = M - i
        update(movie_idx[select], 1)

    print(*result)