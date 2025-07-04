def min_flips_optimized(s):
    if not s:
        return 0
    
    groups = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            groups += 1
    
    return groups // 2

s = input().strip()
print(min_flips_optimized(s))