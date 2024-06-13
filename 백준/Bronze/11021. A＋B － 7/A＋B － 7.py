test_num = int(input())
for i in range(test_num):
    user_li = input().split(' ')
    print(f"Case #{i+1}: {int(user_li[0]) + int(user_li[1])}")