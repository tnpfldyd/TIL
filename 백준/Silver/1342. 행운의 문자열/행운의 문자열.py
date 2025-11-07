import sys
input = sys.stdin.readline

S = input().strip()

def backtrack(path, remaining):
    if not remaining:
        return 1
    
    count = 0
    used = set()
    
    for char in remaining:
        if char in used:
            continue
        if path and path[-1] == char:
            continue
        
        used.add(char)
        new_remaining = list(remaining)
        new_remaining.remove(char)
        count += backtrack(path + char, new_remaining)
    
    return count

print(backtrack("", list(S)))