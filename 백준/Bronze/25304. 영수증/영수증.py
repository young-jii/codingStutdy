total_price = int(input())
total_gae = int(input())
cal_price = 0
for i in range(total_gae):
    mul_li = input().split()
    cal_price += (int(mul_li[0]) * int(mul_li[1]))

if cal_price == total_price:
    print('Yes')
else:
    print('No')