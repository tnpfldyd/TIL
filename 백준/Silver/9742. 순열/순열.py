import sys
import math

input = sys.stdin.readline

def kth_permutation(s, k):
    n = len(s)
    if k > math.factorial(n):
        return "No permutation"

    chars = list(s)
    k -= 1
    result = []

    for i in range(n, 0, -1):
        f = math.factorial(i - 1)
        idx = k // f
        k %= f
        result.append(chars.pop(idx))

    return "".join(result)

while True:
    try:
        s, k = input().split()
        k = int(k)
        print(f"{s} {k} = {kth_permutation(s, k)}")
    except:
        break