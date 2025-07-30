S = input()

suffixes = []
for i in range(len(S)):
    suffixes.append(S[i:])

suffixes.sort()

for suffix in suffixes:
    print(suffix)