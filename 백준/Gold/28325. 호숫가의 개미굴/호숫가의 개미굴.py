N = int(input())
arr = list(map(int, input().split()))

answer = sum(arr)

if not answer:
    print(N // 2)
else:
    idx = next((i for i, x in enumerate(arr) if x), None)
    arr = arr[idx + 1:] + arr[:idx + 1]

    visited = [False] * N

    for i in range(N):
        if arr[i] or visited[i]:
            continue

        for j in range(i, N):
            if arr[j]:
                break

            visited[j] = True
        answer += (j - i + 1) // 2

    print(answer)