from collections import deque
maps =["AABCA.QA", "AABC..QX", "BBBC.Y..", ".A...T.A", "....EE..", ".M.XXEXQ", "KL.TBBBQ"]
result = 15
matrix = []
for i in maps:
    temp = []
    for j in i:
        if j != '.':
            temp.append(ord(j)-65)
        else:
            temp.append(j)
    matrix.append(temp)
N = len(maps); M = len(maps[0])
dx, dy = [0,0,1,-1],[1,-1,0,0]
visited = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if not visited[i][j] and matrix[i][j] != '.':
            temp = {}
            temp_dic = {}
            visited[i][j] = True
            start = deque()
            start.append((i, j))
            temp_dic[matrix[i][j]] = 1
            temp[matrix[i][j]] = [(i, j)]
            while start:
                x, y = start.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        if matrix[nx][ny] != '.' and not visited[nx][ny]:
                            if matrix[nx][ny] not in temp_dic:
                                temp_dic[matrix[nx][ny]] = 1
                                temp[matrix[nx][ny]] = [(nx, ny)]
                            else:
                                temp_dic[matrix[nx][ny]] += 1
                                temp[matrix[nx][ny]].append((nx, ny))
                            start.append((nx, ny))
                            visited[nx][ny] = True
            max_value = 0
            for k, v in temp_dic.items():
                if v > max_value:
                    max_value = v
            answer = sorted(temp_dic.items(), key = lambda x : (-x[1], -x[0]))
            for k, v in answer:
                if v < max_value:
                    go = temp[k]
                    for z in go:
                        matrix[z[0]][z[1]] = answer[0][0]
result = {}
for i in range(N):
    for j in range(M):
        if matrix[i][j] != '.':
            if matrix[i][j] not in result:
                result[matrix[i][j]] = 1
            else:
                result[matrix[i][j]] += 1
result = sorted(result.items(), key = lambda x : -x[1])
print(result[0][1])