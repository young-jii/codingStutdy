# 1. 변수 입력받기
num_li = input().split(' ')
price = 0
find_num = 0

# 2. 같은 숫자가 입력되었는지 확인하기
# 2-(1). 세 숫자가 모두 같을 경우
if len(set(num_li)) == 1:
    price = 10000 + (int(num_li[0])) * 1000

# 2-(2). 세 숫자 중 두 개가 같을 경우
elif len(set(num_li)) == 2:
    # 같은 눈이 뭔지 찾아야 함
    # 0/1 0/2 1/2 비교해야 함
    for i in range(len(num_li)-1):
        for y in range(i+1, len(num_li)):
            if num_li[i] == num_li[y]:
                find_num = int(num_li[i])

    price = 1000+find_num*100

# 2-(3). 세 숫자가 모두 다를 경우
elif len(set(num_li)) == 3:
    for i in num_li:
        if int(i) > find_num:
            find_num = int(i)
    price = find_num * 100

print(price)