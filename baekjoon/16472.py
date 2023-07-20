N = int(input())
string = input()

alphabet = [0] * 26
left = right = 0
cnt = 1
answer = 0

alphabet[ord(string[0]) - ord('a')] += 1

while right < len(string) - 1:
    right += 1
    if alphabet[ord(string[right]) - ord('a')] == 0:
        cnt += 1
    alphabet[ord(string[right]) - ord('a')] += 1

    while cnt > N and left < right:
        if alphabet[ord(string[left]) - ord('a')] == 1:
            cnt -= 1
        alphabet[ord(string[left]) - ord('a')] -= 1
        left += 1

    answer = max(answer, right - left + 1)

print(answer)