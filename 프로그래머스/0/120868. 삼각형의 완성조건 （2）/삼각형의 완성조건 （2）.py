def solution(sides):
    answer = 0

    # 기존 sides 중에서 큰 값이 최대값인 경우, 
    # max(sides) - min(sides) < samWay <= max(sides)
    # samWay의 개수 >> min(sides)
    
    # 새로운 값이 가장 큰 값일 경우,
    # max(sides) < samway < sum(sides)
    # samWay의 개수 >> sum(sides) - max(sides) - 1
    
    answer = min(sides) + sum(sides) - max(sides) - 1
    
    return answer