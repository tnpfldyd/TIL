s = input()

a = False
for i in range(len(s) // 2):
    if s[i] != s[len(s) - i - 1]:
        print(len(s))
        exit()
    elif s[i] != s[i + 1]:
        a = True
print(len(s) - 1 if a else -1)
