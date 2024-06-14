find_num = input().split(' ')
num_li = input().split(' ')
answer = ''
for i in num_li:
    if int(i) < int(find_num[1]):
        answer += i
        answer += ' ' 
print(answer)