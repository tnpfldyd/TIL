n = int(input())
a = list(map(int, input().split()))
a.sort()

candidates = []

candidates.append(a[-1] * a[-2])
candidates.append(a[0] * a[1])
candidates.append(a[-1] * a[-2] * a[-3])
candidates.append(a[-1] * a[0] * a[1])

print(max(candidates))