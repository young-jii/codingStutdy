def solution(n):
    answer = 0
    # 약수의 개수 구하기
    for i in range(1, n+1, 1):
        if n % i == 0:
            answer += 1
    return answer