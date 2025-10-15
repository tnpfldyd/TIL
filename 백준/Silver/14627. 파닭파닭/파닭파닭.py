import sys
input = sys.stdin.readline

S, C = map(int, input().split())
green_onions = [int(input()) for _ in range(S)]

def count_pieces(length):
    count = 0
    for onion in green_onions:
        count += onion // length
    return count

left, right = 1, max(green_onions)

while left <= right:
    mid = (left + right) // 2
    if count_pieces(mid) >= C:
        left = mid + 1
    else:
        right = mid - 1

result_length = right
total_used = result_length * C

print(sum(green_onions) - total_used)