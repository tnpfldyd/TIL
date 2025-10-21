def find(k, n):
    if k == 0:
        return "moo"[n - 1]

    left = length[k - 1]
    mid = k + 3

    if n <= left:
        return find(k - 1, n)
    elif n == left + 1:
        return "m"
    elif n <= left + mid:
        return "o"
    else:
        return find(k - 1, n - left - mid)
    
N = int(input())

length = [3]
k = 0
while length[-1] < N:
    k += 1
    length.append(length[-1] * 2 + (k + 3))

print(find(k, N))