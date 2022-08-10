Text = input()
happy = Text.count(':-)')
sad = Text.count(':-(')
if happy == 0 and sad == 0:
    print('none')
else:
    if happy > sad:
        print('happy')
    elif sad > happy:
        print('sad')
    else:
        print('unsure')