L, K, C = map(int, input().split())
posit = [0] + sorted(map(int, input().split())) + [L]
pieces = [posit[i + 1] - posit[i] for i in range(K+1)][::-1]
max_piece = max(pieces)

left, right = 0, L

def cutting(x):
    if max_piece > x:
        return C+1, 0
    total, count = 0, 0
    for piece in pieces:
        total += piece
        if total > mid:
            total = piece
            count += 1
    return count, total if count == C else pieces[-1]
while left <= right:
    mid = (left + right) // 2
    cnt, result = cutting(mid)
    if C < cnt:
        left = mid + 1
    else:
        answer = mid
        start = result
        right = mid - 1
print(answer, start)