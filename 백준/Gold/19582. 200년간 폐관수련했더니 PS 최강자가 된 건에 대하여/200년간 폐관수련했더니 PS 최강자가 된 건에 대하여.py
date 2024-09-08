import sys
input = sys.stdin.readline

def main():
    N = int(input())
    max_p = 0
    absence = 0
    reward = 0

    for _ in range(N):
        x, p = map(int, input().split())
        if reward <= x:
            reward += p
            max_p = max(max_p, p)
        elif reward - max_p > x or max_p < p:
            absence += 1
        else:
            reward -= max_p
            reward += p
            absence += 1

        if absence == 2:
            print("Zzz")
            return

    print("Kkeo-eok")

if __name__ == "__main__":
    main()