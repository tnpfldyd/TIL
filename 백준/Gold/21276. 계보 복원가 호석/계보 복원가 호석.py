import sys
input = sys.stdin.readline

N = int(input())
names = input().split()
name2id = {name: i for i, name in enumerate(names)}

anc = [set() for _ in range(N)]
M = int(input())
for _ in range(M):
    x, y = input().split()
    anc[name2id[x]].add(name2id[y])

depth = [len(anc[i]) for i in range(N)]
children = [[] for _ in range(N)]
for i in range(N):
    if depth[i] > 0:
        for j in anc[i]:
            if depth[j] == depth[i] - 1:
                children[j].append(i)
                break

roots = [i for i in range(N) if depth[i] == 0]
root_names = sorted(names[i] for i in roots)

print(len(root_names))
print(*root_names)
for i in sorted(range(N), key=lambda i: names[i]):
    c = sorted(names[j] for j in children[i])
    print(names[i], len(c), *c)