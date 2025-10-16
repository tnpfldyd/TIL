N, k = map(int, input().split())
K = list(map(str, input().split()))

N_str = str(N)
max_result = 0

def dfs(num_str):
    global max_result
    if num_str:
        num = int(num_str)
        if num <= N:
            max_result = max(max_result, num)
        else:
            return

    if len(num_str) > len(N_str):
        return

    for digit in K:
        dfs(num_str + digit)

dfs("")
print(max_result)