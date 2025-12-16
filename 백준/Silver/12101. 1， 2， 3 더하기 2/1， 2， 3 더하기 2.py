n, k = map(int, input().split())

result = []
count = 0
found = False

def dfs(current_sum):
    global count, found

    if current_sum == n:
        count += 1
        if count == k:
            print('+'.join(map(str, result)))
            found = True
        return

    if current_sum > n or found:
        return

    for num in (1, 2, 3):
        result.append(num)
        dfs(current_sum + num)
        result.pop()

dfs(0)

if not found:
    print(-1)