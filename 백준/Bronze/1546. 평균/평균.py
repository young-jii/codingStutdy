# 과목수 작성하기
subject_num = int(input())
# 평균 점수 입력하기
score = input().split(' ')
int_score = [int(i) for i in score]
# 최고점 확인하기
max_score = max(int_score)
new_score = []
# 점수 새로 계산하기
for y in int_score:
    new_score.append(y/max_score*100)
# 새로운 평균 계산하기
print(sum(new_score) / subject_num)