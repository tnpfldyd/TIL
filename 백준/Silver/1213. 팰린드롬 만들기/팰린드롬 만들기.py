def make_palindrome(name):
    char_count = {}
    for char in name:
        char_count[char] = char_count.get(char, 0) + 1
    
    odd_count = 0
    odd_char = ''
    for char, count in char_count.items():
        if count % 2 == 1:
            odd_count += 1
            odd_char = char
    
    if odd_count > 1:
        return "I'm Sorry Hansoo"
    
    left_half = []
    for char in sorted(char_count.keys()):
        left_half.extend([char] * (char_count[char] // 2))
    
    palindrome = left_half[:]
    
    if odd_count == 1:
        palindrome.append(odd_char)
    
    palindrome.extend(left_half[::-1])
    
    return ''.join(palindrome)

name = input().strip()

result = make_palindrome(name)
print(result)