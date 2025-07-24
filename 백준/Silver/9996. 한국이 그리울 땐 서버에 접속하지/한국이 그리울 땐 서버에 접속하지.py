import sys
input = sys.stdin.readline

n = int(input())
pattern = input().strip()

star_pos = pattern.index('*')
prefix = pattern[:star_pos]
suffix = pattern[star_pos + 1:]

for _ in range(n):
    filename = input().strip()
    
    if len(filename) < len(prefix) + len(suffix):
        print("NE")
        continue
    
    if filename.startswith(prefix) and filename.endswith(suffix):
        middle_start = len(prefix)
        middle_end = len(filename) - len(suffix)
        
        if middle_start <= middle_end:
            print("DA")
        else:
            print("NE")
    else:
        print("NE")