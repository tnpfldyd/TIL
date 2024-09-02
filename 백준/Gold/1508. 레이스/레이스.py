def main():
    n, m, k = map(int, input().split())
    positions = list(map(int, input().split()))

    left, right = 1, positions[-1] - positions[0]
    optimal_distance = -1

    while left <= right:
        mid = (left + right) // 2
        last_position = positions[0]
        judges_count = 1

        for i in range(1, k):
            if positions[i] - last_position >= mid:
                last_position = positions[i]
                judges_count += 1

        if judges_count >= m:
            optimal_distance = mid
            left = mid + 1
        else:
            right = mid - 1

    last_position = positions[0]
    judges_count = 1
    result = ['1']

    for i in range(1, k):
        if (positions[i] - last_position >= optimal_distance) and (judges_count < m):
            result.append('1')
            judges_count += 1
            last_position = positions[i]
        else:
            result.append('0')

    print(''.join(result))


if __name__ == "__main__":
    main()