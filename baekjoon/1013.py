import sys, re
input = sys.stdin.readline
pattern = "(100+1+|01)+"
print("\n".join(["YES" if re.fullmatch(pattern, input().strip()) else "NO" for _ in range(int(input()))]))