import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = input().strip()

people = []
hamburgers = []

for i in range(n):
    if s[i] == 'P':
        people.append(i)
    else:
        hamburgers.append(i)

used = [False] * len(hamburgers)
count = 0
h_idx = 0

for person in people:
    while h_idx < len(hamburgers) and hamburgers[h_idx] < person - k:
        h_idx += 1
    
    temp_idx = h_idx
    while temp_idx < len(hamburgers) and hamburgers[temp_idx] <= person + k:
        if not used[temp_idx]:
            used[temp_idx] = True
            count += 1
            break
        temp_idx += 1

print(count)