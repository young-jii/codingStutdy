def solution(myString, pat):
    answer = 0
    changeString = ''
    for i in myString:
        if i == "A":
            changeString += "B"
        elif i == "B":
            changeString += "A"
    if pat in changeString:
        answer = 1
    return answer