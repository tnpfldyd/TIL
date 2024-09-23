import sys

input = sys.stdin.readline

def clean_room(x, y):
    global trash_count, room
    if x == rows - 1 and y == cols - 1:
        if room[x][y] == 1:
            trash_count -= 1
            room[x][y] = 0        
        return
    for i in range(x, rows):
        for j in range(y, cols):
            if room[i][j] == 1:
                room[i][j] = 0
                trash_count -= 1
                clean_room(i, j)              
                return
    return

rows, cols = map(int, input().split())
room = []
trash_count = 0
cleaning_count = 0

for _ in range(rows):
    row = list(map(int, input().split()))
    room.append(row)
    trash_count += sum(row)

while trash_count > 0:
    cleaning_count += 1
    if room[0][0] == 1:
        room[0][0] = 0
        trash_count -= 1
    clean_room(0, 0)

print(cleaning_count)
