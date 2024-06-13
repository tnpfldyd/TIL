import sys
import math

def find_one(k):
    visited = [False] * (N + 1)
    find = [0] * N
    for i in range(N):
        for j in range(1, N + 1):
            if not visited[j]:
                if i + 1 < N:
                    if case[i + 1] >= k:
                        find[i] = j
                        visited[j] = True
                        break
                    else:
                        k -= case[i + 1]
                else:
                    find[i] = j
    return find

def find_k(sequence):
    visited = [False] * (N + 1)
    order = 1
    idx = 1
    for i in sequence:
        tmp = 0
        for j in range(1, N + 1):
            if not visited[j]:
                tmp += 1
                if i == j:
                    break
        if idx < N:
            order += (tmp - 1) * case[idx]
        idx += 1
        visited[i] = True
    return order

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    problem = list(map(int, input().split()))
    case = [0] * N
    case[0] = math.factorial(N)
    for i in range(1, N):
        case[i] = case[i - 1] // (N + 1 - i)

    if problem[0] == 1:
        k = problem[1]
        print(*find_one(k))
    else:
        sequence = problem[1:]
        print(find_k(sequence))
