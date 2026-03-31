from itertools import pairwise

s = input()
print(10 + sum(5 if a == b else 10 for a, b in pairwise(s)))