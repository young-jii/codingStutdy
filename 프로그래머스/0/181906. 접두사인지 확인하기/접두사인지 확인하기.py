def solution(my_string, is_prefix):
    answer = 0
    pre_len = len(is_prefix)
    if is_prefix in my_string[:pre_len]:
        answer = 1
    return answer