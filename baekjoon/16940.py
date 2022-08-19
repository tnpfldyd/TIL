from collections import deque
import sys
input = sys.stdin.readline
def bfs(start):
    dec = deque()
    result = [1]
    dec.append(start)
    visited[start] = True
    while dec:
        x = dec.popleft()
        for i in mat[x]:
            if not visited[i]:
                result.append(i)
                dec.append(i)
                visited[i] = True
    return result
T = int(input())
visited = [False] * (T+1)
mat = [[] for _ in range(T+1)]
prev = []
for i in range(T):
    A = list(map(int, input().rstrip().split()))
    if i == T-1:
        if A[0] != 1:
            print(0)
            sys.exit(0)
        prev = A
    else:
        mat[A[0]].append(A[1])
        mat[A[1]].append(A[0])

rev = [0] * (T+1)
for j in range(len(prev)):
    # 문제에서 주어진 수들의 순서대로 번호를 매김 
    # 예) prev[1,7,6,2,10,9,8,4,3,5] - rev = [0,0,3,8,7,9,2,1,6,5,4] = 
    # 1은 0번째 2은 3번째 3은 8번째 순서라는 뜻
    rev[prev[j]] = j 
for k in range(1, len(mat)):
    # 위의 rev 순서를 바탕으로 탐색해야 하는 순서(간선)를 정렬해줌
    # bfs 는 답이 여러개가 존재할 수 있기때문에 1가지 경우만 보면 안됨.
    # 주어진 리스트가 정답인지 체크해야하기 때문에 그 순서를 바탕으로 검사
    mat[k].sort(key = lambda x : rev[x]) # mat[1] = 2,7,6 이었다면 7,6,2 순으로 정렬해줌 prev의 순서대로 정렬함
rere = bfs(1)
print(1 if rere == prev else 0)