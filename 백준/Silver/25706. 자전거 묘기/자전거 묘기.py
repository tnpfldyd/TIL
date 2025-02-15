import sys

def min_jumps(N, jumps):
    sol = [1]
    for i in range(N - 1, 0, -1):
        target_index = N - i - jumps[i - 1] - 1
        if target_index >= 0:
            sol.append(sol[target_index] + 1)
        else:
            sol.append(1)
    
    sol.reverse()
    print(*sol)

if __name__ == "__main__":
    N = int(input())
    jumps = list(map(int, sys.stdin.readline().split()))
    min_jumps(N, jumps)