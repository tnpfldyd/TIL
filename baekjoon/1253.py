def main():
    num = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    result = 0
    for i in range(num):
        val = arr[i]
        l = 0
        r = num - 1
        sum = 0

        while l < r:
            sum = arr[l] + arr[r]
            if sum == val:
                if l != i and r != i:
                    result += 1
                    break
                elif l == i:
                    l += 1
                else:
                    r -= 1
            elif sum < val:
                l += 1
            else:
                r -= 1

    print(result)

if __name__ == "__main__":
    main()