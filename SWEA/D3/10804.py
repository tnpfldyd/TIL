import sys
sys.stdin = open('10804input.txt', 'r')
T = int(input())
for i in range(1, T+1):
    word = input()
    word = list(word)
    new_word = []
    for j in range(len(word)):
        if word[j] == 'b':
            word[j] = 'd'
        elif word[j] == 'd':
            word[j] = 'b'
        elif word[j] == 'q':
            word[j] = 'p'
        else:
            word[j] = 'q'
    
    print(f'#{i}', ''.join(word[::-1]))