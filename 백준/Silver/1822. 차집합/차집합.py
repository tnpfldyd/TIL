n_A, n_B = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

result = A - B

print(len(result))
if result:
    print(*sorted(result))