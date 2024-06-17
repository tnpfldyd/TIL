def dfs(current_num, current_count, result_list, num_list):
    if current_count == len(num_list):
        print(" ".join(map(str, result_list)))
        exit(0)

    if current_num % 3 == 0 and current_num // 3 in num_list:
        result_list.append(current_num // 3)
        dfs(current_num // 3, current_count + 1, result_list, num_list)
        result_list.pop()
    if 2 * current_num in num_list:
        result_list.append(2 * current_num)
        dfs(2 * current_num, current_count + 1, result_list, num_list)
        result_list.pop()
    return

n = int(input())
num_list = list(map(int, input().split()))

for num in num_list:
    dfs(num, 1, [num], num_list)
