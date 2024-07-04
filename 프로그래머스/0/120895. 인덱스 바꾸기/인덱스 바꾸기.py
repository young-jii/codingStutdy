def solution(my_string, num1, num2):
    answer = ''
    s_li = list(my_string)
    s_li[num1], s_li[num2] = s_li[num2], s_li[num1]
    answer = ''.join(s_li)
    return answer