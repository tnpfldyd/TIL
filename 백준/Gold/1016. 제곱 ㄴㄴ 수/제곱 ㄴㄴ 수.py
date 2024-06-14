def count_sq_free(min_v, max_v):
    size = max_v - min_v + 1
    sq_free = [True] * size

    max_sqrt = int(max_v ** 0.5) + 1
    for i in range(2, max_sqrt):
        sq = i * i
        start = (min_v + sq - 1) // sq * sq
        for j in range(start, max_v + 1, sq):
            sq_free[j - min_v] = False

    count = sum(sq_free)
    return count

min_v, max_v = map(int, input().split())
print(count_sq_free(min_v, max_v))

