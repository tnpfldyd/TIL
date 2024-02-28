N = int(input())
numbers = list(map(int, input().split()))
left = right = 0
answer = 1

while left <= right and right < N - 1:
    if numbers[right] < numbers[right + 1]:
        right += 1
        continue

    length = 0

    if numbers[right] == numbers[right + 1]:
        while length <= right - left:
            if right + 1 + length >= N or numbers[right - length] != numbers[right + 1 + length]:
                break
            length += 1
        answer = max(answer, 2 * length)
    else:
        while length < right - left:
            if right + 1 + length >= N or numbers[right - 1 - length] != numbers[right + 1 + length]:
                break
            length += 1
        answer = max(answer, 2 * length + 1)
    left = right + 1
    right += 1

print(answer)