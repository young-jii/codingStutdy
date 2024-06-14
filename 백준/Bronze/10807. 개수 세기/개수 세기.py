# 변수 작성
input_num = int(input())
# input_num 개의 숫자 작성
num_li = input().split(' ')
# 찾을 숫자 변수 작성
find_num = input()

## 개수 찾기
cnt = 0
for i in num_li:
    if i == find_num:
        cnt += 1

print(cnt)