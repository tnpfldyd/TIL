while True:
    Text = input()
    if Text != '#':
        cnt = 0
        for T in Text:
            if T in 'aeiouAEIOU':
                cnt += 1
        print(cnt)
    else:
        break