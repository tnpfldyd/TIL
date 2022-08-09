import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
N += 1

matrix = [[] for _ in range(N)] # 리스트 생성
for _ in range(M):
    v1, v2 = map(int, input().rstrip().split())
    matrix[v1].append(v2)
    matrix[v2].append(v1)
start = []
for i in matrix[1]:
    start.append(i) # 1번 컴퓨터 부터 감염 된 컴퓨터 start 통에 저장
result = set() # 중복 제거하기 위함
while start: # start 통이 비기 전까지 순회
    virus = start.pop(0) # 연결된 컴퓨터 하나씩 검사
    for i in matrix[virus]:
        if i not in result: # 이미 set 에 추가 했으면 제외
            start.append(i)
        result.add(i)
if 1 in result:
    print(len(result) - 1)
else:
    print(len(result))

