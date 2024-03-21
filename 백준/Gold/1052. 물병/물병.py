n, k = map(int, input().split())
cnt = 0
def count_ones_in_binary(x):
    count = 0
    while x:
        count += x & 1
        x >>= 1
    return count

while count_ones_in_binary(n) > k:
    n += 1
    cnt += 1

print(cnt)