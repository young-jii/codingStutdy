def solution(a, b):
    answer = 0
    plusone = int(str(a)+str(b)) 
    gap = 2 * a * b
    
    if plusone > gap:
        answer = plusone
    elif plusone < gap:
        answer = gap
    else:
        answer = a + b
    return answer