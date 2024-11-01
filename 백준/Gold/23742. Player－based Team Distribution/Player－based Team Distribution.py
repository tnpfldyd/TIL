def main():
    import sys
    input = sys.stdin.readline

    N = int(input().strip())
    positive_numbers = []
    negative_numbers = []
    positive_sum = 0
    negative_sum = 0
    nums = list(map(int, input().strip().split()))
    for i in range(1, N + 1):
        t = nums[i - 1]
        if t < 0:
            negative_numbers.append(t)
            negative_sum += t
        else:
            positive_numbers.append(t)
            positive_sum += t

    answer = (positive_sum * len(positive_numbers)) + negative_sum

    negative_numbers.sort()

    positive_count = len(positive_numbers)
    for i in range(len(negative_numbers) - 1, -1, -1):
        positive_count += 1
        negative_sum -= negative_numbers[i]
        positive_sum += negative_numbers[i]

        answer = max(answer, positive_sum * positive_count + negative_sum)

    print(answer)

if __name__ == "__main__":
    main()
