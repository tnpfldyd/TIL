import sys
input = sys.stdin.readline

N = int(input())
machines = list(map(int, input().split()))

machines.sort()

max_loss = 0

if N % 2 == 1:
    max_loss = machines[-1]
    machines = machines[:-1]

for i in range(len(machines) // 2):
    loss = machines[i] + machines[-(i+1)]
    max_loss = max(max_loss, loss)

print(max_loss)