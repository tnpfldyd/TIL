import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    curr = 0
    left = right = 0
    while True:
        if curr >= m:
            if curr == m:
                count += 1
            curr -= a[left]
            left += 1
        else:
            if right == n:
                break
            curr += a[right]
            right += 1
    print(count)

if __name__ == "__main__":
    main()