MAX_DISTANCE = 1001

input_str = input()
target_str = input()

len_input = len(input_str)
len_target = len(target_str)

edit_distance = [[0] * (len_target + 1) for _ in range(len_input + 1)]

for i in range(1, len_input + 1):
    edit_distance[i][0] = i

for j in range(1, len_target + 1):
    edit_distance[0][j] = j

for i in range(1, len_input + 1):
    for j in range(1, len_target + 1):
        if input_str[i-1] == target_str[j-1]:
            edit_distance[i][j] = edit_distance[i-1][j-1]
        else:
            edit_distance[i][j] = min(edit_distance[i-1][j], edit_distance[i][j-1], edit_distance[i-1][j-1]) + 1

print(edit_distance[len_input][len_target])
