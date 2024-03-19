def find(current):
    global result
    for button in button_set:
        temp = current + str(button)
        result = min(result, abs(N - int(temp)) + len(temp))

        if len(temp) < 6:
            find(temp)

N = int(input())
M = int(input())
button_set = {i for i in range(10)}
result = abs(N - 100)
button_set -= set(map(int, input().split(' '))) if M else set()
find('') if M < 10 else ''
print(result)