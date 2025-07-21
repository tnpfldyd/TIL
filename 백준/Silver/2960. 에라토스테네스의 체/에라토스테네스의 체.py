def find_kth_erased(n, k):
    erased = [False] * (n + 1)
    count = 0
    
    for i in range(2, n + 1):
        if not erased[i]:
            for j in range(i, n + 1, i):
                if not erased[j]:
                    erased[j] = True
                    count += 1
                    if count == k:
                        return j

n, k = map(int, input().split())
print(find_kth_erased(n, k))