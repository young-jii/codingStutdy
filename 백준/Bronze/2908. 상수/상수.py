num_li = input().split(' ')
num1 = int(num_li[0][::-1])
num2 = int(num_li[1][::-1])
if num1 > num2 :
    print(num1)
else:
    print(num2)