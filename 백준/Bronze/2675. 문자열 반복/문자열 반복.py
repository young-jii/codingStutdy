num = int(input())
for i in range(num):
    check_li = input().split()
    answer = ''
    for y in check_li[1]:
        answer += (y * int(check_li[0]))
    print(answer)