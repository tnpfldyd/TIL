lights = input().strip()
N = len(lights)

state = [1 if c == 'Y' else 0 for c in lights]
count = 0

for i in range(1, N + 1):
    if state[i - 1] == 1:
        count += 1

        for j in range(i - 1, N, i):
            state[j] ^= 1

print(count)