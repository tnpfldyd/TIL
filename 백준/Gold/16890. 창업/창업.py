from collections import deque

sorted_list1 = sorted(list(input().strip()))
sorted_list2 = sorted(list(input().strip()), reverse=True)
N = len(sorted_list1)

first_half = deque(sorted_list1[:N - N // 2])
second_half = deque(sorted_list2[:N // 2])
result_list = [''] * N
left_index, right_index = 0, N - 1
turn = 1

for _ in range(N):
    current_list = first_half if turn == 1 else second_half

    if first_half and second_half and first_half[0] >= second_half[0]:
        result_list[right_index] = current_list.pop()
        right_index -= 1
    else:
        result_list[left_index] = current_list.popleft()
        left_index += 1

    turn = -turn

print(''.join(result_list))
