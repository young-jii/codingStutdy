num_li = input().split(' ')

basket = int(num_li[0])
putIn = int(num_li[1])

basket_li = ['0' for i in range(basket)]
# print(basket_li)

for i in range(putIn):
    num_ball = input().split(' ')
    # print(num_ball)
    for y in range(int(num_ball[0])-1, int(num_ball[1])):
        basket_li[y] = num_ball[2]

print(' '.join(basket_li))
