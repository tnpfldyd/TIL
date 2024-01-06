import itertools
N = int(input())
numbers = reversed(list(range(10)))
for permutation in itertools.permutations(numbers, 7):
    d, e, h, l, o, r, w = permutation
    if not h or not w:
        continue
    hello = 10000 * h + 1000 * e + 100 * l + 10 * l + o
    world = 10000 * w + 1000 * o + 100 * r + 10 * l + d
    if hello + world == N:
        print(f'  {hello}')
        print(f'+ {world}')
        print("-------")
        print(f' {N}' if len(str(N)) > 5 else f'  {N}')
        break
else:
    print('No Answer')
