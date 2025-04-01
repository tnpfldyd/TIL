import sys

T = int(sys.stdin.readline())

for _ in range(T):
    recorded = sys.stdin.readline().strip().split()
    known_sounds = set()
    
    while True:
        line = sys.stdin.readline().strip()
        if line == "what does the fox say?":
            break
        parts = line.split()
        known_sounds.add(parts[2])
    
    fox_sounds = [sound for sound in recorded if sound not in known_sounds]
    print(' '.join(fox_sounds))