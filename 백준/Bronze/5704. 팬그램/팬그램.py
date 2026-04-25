import sys
input = sys.stdin.readline

while True:
    sentence = input().rstrip()

    if sentence == '*':
        break

    if len(set(sentence.replace(' ', ''))) == 26:
        print('Y')
    else:
        print('N')