import sys
input = sys.stdin.readline

scenario = 1

while True:
    n = int(input())

    if n == 0:
        break

    names = [input().rstrip('\n') for _ in range(n)]

    count = [0] * (n + 1)

    for _ in range(2 * n - 1):
        num, _ = input().split()
        count[int(num)] += 1

    for i in range(1, n + 1):
        if count[i] % 2 == 1:
            print(scenario, names[i - 1])
            break

    scenario += 1