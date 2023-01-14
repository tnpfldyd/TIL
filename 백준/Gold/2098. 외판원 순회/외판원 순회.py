import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
matrix = [list(map(int, input().strip().split())) for _ in range(N)]
cost = [[-1] * (2 ** N) for _ in range(N)]
answer = bin((2 ** N) - 1)[2:]

def dfs(node, bit):
    if bit == answer:
        return matrix[node][0] or INF

    if cost[node][int(bit, 2)] != -1:
        return cost[node][int(bit, 2)]
    
    dist = INF
    for i in range(1, N):
        if matrix[node][i] and bit[abs(i+1-N)] == '0':
            key = list('0' * N)
            key[abs(i+1-N)] = '1'
            new_key = ''
            for j in range(N):
                if bit[j] == '1' or key[j] == '1':
                    new_key += '1'
                else:
                    new_key += '0'
            dist = min(dist, dfs(i, new_key) + matrix[node][i])
    cost[node][int(bit,2)] = dist
    return cost[node][int(bit, 2)]
key = list('0'*N)
key[-1] = '1'
print(dfs(0, ''.join(key)))
