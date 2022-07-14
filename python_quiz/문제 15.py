a = 'bbba'
b = 0
for c in a:
    if c in 'a':
        print(b)
        break

    elif not 'a' in a:
        print(-1)
        break
    
    else:
        b += 1    
    