a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and(not d)) or ((not c) and d))

a, b = map(int, input().split())
print(bool(a and (not b)) or bool((not a) and b))