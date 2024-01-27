s = input()
p = input()
cnt = 0

i = 0
while i < len(p):
    max_len = 0
    for j in range(len(s)):
        temp = 0
        while j + temp < len(s) and i + temp < len(p) and s[j + temp] == p[i + temp]:
            temp += 1
        max_len = max(max_len, temp)
    
    i += max_len
    cnt += 1

print(cnt)