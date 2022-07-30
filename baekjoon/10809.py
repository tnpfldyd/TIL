alpabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
text = input()
for i in range(len(alpabet)):
    if alpabet[i] in text:
        print(text.index(alpabet[i]), end = ' ')
    else:
        print('-1', end = ' ')