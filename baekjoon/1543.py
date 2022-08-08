Text = input()
Text_in = input()
X = 0
cnt = 0
while X <= len(Text) - len(Text_in):
    if Text[X : X + len(Text_in)] == Text_in:
        cnt += 1
        X += len(Text_in)
    else:
        X += 1
print(cnt)