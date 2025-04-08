def main():
    import sys
    input = sys.stdin.readline
    n = int(input())
    for _ in range(n):
        data = list(map(int, input().split()))
        T = data[0]
        soldiers = data[1:]
        counts = {}
        for num in soldiers:
            counts[num] = counts.get(num, 0) + 1
        found = False
        for army, count in counts.items():
            if count > T / 2:
                print(army)
                found = True
                break
        if not found:
            print("SYJKGW")

if __name__ == "__main__":
    main()