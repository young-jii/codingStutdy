# 1. 변수 설정
time_now = input().split(' ')
time_cook = int(input())
# 1-(1). 입력 받은 현재 시간 >> 분 초로 구분하기
now_H = int(time_now[0])
now_M = int(time_now[1])
# 1-(2). 요리 시간 >> 분 초로 구분하기
cook_H = time_cook // 60
cook_M = time_cook % 60
# 1-(3). 최종 시간 변수 설정하기
final_H = 0
final_M = 0

# 2. 시간 계산하기
final_H = now_H + cook_H
final_M = now_M + cook_M

# 3. 조건 반영하기
if final_M >= 60:
    final_H = final_H + (final_M // 60)
    final_M = final_M % 60

if final_H >= 24:
    final_H = final_H % 24

print(str(final_H) + ' ' + str(final_M) )
