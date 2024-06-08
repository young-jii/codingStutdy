# [방법2] 두 숫자의 빈도 계산 > 리스트 형성 > 결과를 기준으로 결과값 도출
def solution(X, Y):
    # 각 숫자의 빈도를 계산하는 리스트 형성
    count_X = [0] * 10
    count_Y = [0] * 10
    # X, Y 숫자의 빈도를 계산해서 만들어 둔 리스트에 넣기
    for i in X:
        count_X[int(i)] += 1
    for j in Y:
        count_Y[int(j)] += 1
    # result 리스트에 X, Y 빈도수 계산 된 것들 중 작은 것 기준으로 추가 >> 큰 수부터 출력
        # - 0만 있다면 0 출력
        # - 리스트가 비어있다면 -1 출력
    result = []
    for k in range(9, -1, -1):
        min_c = min(count_X[k], count_Y[k])
        result.extend(str(k) * min_c)
    
    if result == []:
        answer = "-1"
        
    elif set(result) == {"0"}:
        answer = "0"
    
    else:
        answer = ''.join(result)
    
    return answer


# [방법1] 리스트와 자료형의 type을 통해서 일일이 작업을 진행한 함수
# def solution(X, Y):
#     answer = ''
#     answer_li = []
    
#     # y 값을 list로 바꿈 → 이후 제거를 위함
#     list_y = [Y[i] for i in range(len(Y))]

#     for i in range(len(X)):
#         # 만약 X의 한 글자가 list로 수정한 Y값 안에 있다면,
#         if X[i] in list_y:
#             # answer_li에 해당 값을 넣기.
#             answer_li.append(int(X[i]))
#             # 넣은 후 중복을 피하기 위해 해당 글자 list에서 삭제.
#             list_y.remove(X[i])
    
#     # answer_li에 값이 아무것도 없다면,
#     if answer_li == []:
#         # 답 = -1
#         answer = '-1'
#     # answer_li에 값이 모두 0이라면,
#     elif all(x==0 for x in answer_li):
#         # 답 = 0
#         answer = '0'
#     # answer_li에 값이 숫자라면,
#     else:
#         # 답 = 오름차순 한 숫자를 문자열로 표현
#         answer_li = [str(x) for x in sorted(answer_li, reverse=True)]
#         answer = ''.join(answer_li)
    
#     return answer