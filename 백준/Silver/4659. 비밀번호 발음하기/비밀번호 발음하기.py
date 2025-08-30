import sys
input = sys.stdin.readline

def is_vowel(c):
    return c in 'aeiou'

def is_acceptable(password):

    has_vowel = any(is_vowel(c) for c in password)
    if not has_vowel:
        return False

    for i in range(len(password) - 2):
        if is_vowel(password[i]) and is_vowel(password[i + 1]) and is_vowel(password[i + 2]):
            return False
        if not is_vowel(password[i]) and not is_vowel(password[i + 1]) and not is_vowel(password[i + 2]):
            return False

    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            if password[i] not in 'eo':
                return False
    
    return True

while True:
    password = input().strip()
    if password == 'end':
        break
    
    if is_acceptable(password):
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")