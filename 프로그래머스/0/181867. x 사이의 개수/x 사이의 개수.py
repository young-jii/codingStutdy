def solution(myString):
    split_string = myString.split('x')
    answer = [len(i) for i in split_string]
    return answer