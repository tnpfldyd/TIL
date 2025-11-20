import sys
input = sys.stdin.readline

def generate_anagrams(word):
    word = sorted(word)
    anagrams = []
    
    def backtrack(path, remaining):
        if not remaining:
            anagrams.append(path)
            return
        
        used = set()
        for i, char in enumerate(remaining):
            if char in used:
                continue
            used.add(char)
            new_remaining = remaining[:i] + remaining[i+1:]
            backtrack(path + char, new_remaining)
    
    backtrack("", word)
    return anagrams

N = int(input())
for _ in range(N):
    word = input().strip()
    anagrams = generate_anagrams(word)
    for anagram in anagrams:
        print(anagram)