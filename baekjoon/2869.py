import math
a, b, c = list(map(int, input().split()))
d = math.ceil((c-b) / (a-b))
print(d)