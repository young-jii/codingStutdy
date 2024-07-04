txt = input()
alpha_char = 'abcdefghijklmnopqrstuvwxyz'
list_alpha = list(alpha_char)
answer = []
for i in list_alpha:
    if i in txt:
        answer.append(str(txt.find(i)))
    else:
        answer.append('-1')
print(' '.join(answer))