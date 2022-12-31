from collections import deque
commands = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap",
"UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 32 korean",
"UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta",
"UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4",
"UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4"]
matrix = [[[] for _ in range(51)] for _ in range(51)]
dx,dy = [0,0,1,-1],[-1, 1,0,0]
answer = []
for i in commands:
    i = i.split()
    if i[0] == 'UPDATE':
        if len(i) == 4:
            if matrix[int(i[1])][int(i[2])] == [] or matrix[int(i[1])][int(i[2])][1] == 0:
                matrix[int(i[1])][int(i[2])] = [i[3],0]
            if matrix[int(i[1])][int(i[2])][1] == 1:
                start = deque()
                temp = set()
                start.append((int(i[1]), int(i[2])))
                temp.add((int(i[1]), int(i[2])))
                while start:
                    x, y = start.popleft()
                    for j in range(4):
                        nx, ny = x + dx[j], y + dy[j]
                        if 0 <= nx < 51 and 0 <= ny < 51:
                            if matrix[nx][ny] == matrix[int(i[1])][int(i[2])] and (nx, ny) not in temp:
                                temp.add((nx, ny))
                                start.append((nx, ny))
                for x, y in temp:
                    matrix[x][y][0] = i[3]
        if len(i) == 3:
            for x in range(51):
                for y in range(51):
                    if len(matrix[x][y]) == 2:
                        if matrix[x][y][0] == i[1]:
                            matrix[x][y][0] = i[2]
    elif i[0] == 'MERGE':
        temp2 = []
        if matrix[int(i[1])][int(i[2])] != [] and matrix[int(i[3])][int(i[4])] != []:
            if matrix[int(i[1])][int(i[2])][1] == 1 and matrix[int(i[3])][int(i[4])][1] == 1:
                temp3 = [matrix[int(i[3])][int(i[4])][0],1]
                start = deque()
                temp = set()
                start.append((int(i[3]), int(i[4])))
                temp.add((int(i[3]), int(i[4])))
                while start:
                    x, y = start.popleft()
                    for j in range(4):
                        nx, ny = x + dx[j], y + dy[j]
                        if 0 <= nx < 51 and 0 <= ny < 51:
                            if matrix[nx][ny] == matrix[int(i[3])][int(i[4])] and (nx, ny) not in temp:
                                temp.add((nx, ny))
                                start.append((nx, ny))
                for x, y in temp:
                    matrix[x][y] = matrix[int(i[1])][int(i[2])]
        else:
            if matrix[int(i[1])][int(i[2])] != [] and matrix[int(i[3])][int(i[4])] != []:
                temp2 = [matrix[int(i[1])][int(i[2])][0], 1]
            elif matrix[int(i[1])][int(i[2])] == [] and matrix[int(i[3])][int(i[4])] != []:
                temp2 = [matrix[int(i[3])][int(i[4])][0], 1]
            elif matrix[int(i[1])][int(i[2])] != [] and matrix[int(i[3])][int(i[4])] == []:
                temp2 = [matrix[int(i[1])][int(i[2])][0], 1]
            if int(i[1]) <= int(i[3]) and int(i[2]) <= int(i[4]):
                for x in range(int(i[1]), int(i[3]) + 1):
                    for y in range(int(i[2]), int(i[4]) + 1):
                        matrix[x][y] = temp2
            else:
                for x in range(int(i[3]), int(i[1]) + 1):
                    for y in range(int(i[4]), int(i[2]) + 1):
                        matrix[x][y] = temp2
    elif i[0] == 'UNMERGE':
        temp3 = [matrix[int(i[1])][int(i[2])][0],0]
        start = deque()
        temp = set()
        start.append((int(i[1]), int(i[2])))
        temp.add((int(i[1]), int(i[2])))
        while start:
            x, y = start.popleft()
            for j in range(4):
                nx, ny = x + dx[j], y + dy[j]
                if 0 <= nx < 51 and 0 <= ny < 51:
                    if matrix[nx][ny] == matrix[int(i[1])][int(i[2])] and (nx, ny) not in temp:
                        temp.add((nx, ny))
                        start.append((nx, ny))
        for x, y in temp:
            matrix[x][y] = []
        matrix[int(i[1])][int(i[2])] = temp3
    else:
        if matrix[int(i[1])][int(i[2])] == []:
            answer.append('EMPTY')
        else:
            answer.append(matrix[int(i[1])][int(i[2])][0])
print(answer)