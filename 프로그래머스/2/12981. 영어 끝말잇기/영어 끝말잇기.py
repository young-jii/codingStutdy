# import math

def solution(n, words):
    answer = [0, 0]
    
    # 확인해야 하는 조건
        # 1. 앞 단어의 끝 글자와 뒷 단어의 첫 글자가 일치하는 지 확인하기
            # > 단어의 순서를 확인하기 위해서는 단어를 보는 것 보다, 단어의 위치를 보는 것이 좋다.
            # > 해당 단어의 앞/뒤 단어를 확인하기 위해서 전체 길이의 -1까지 for 문을 돌려야 한다.
        # 2. 특정 단어가 기존에 없는 단어인지 확인하기
    
    # [방법2] count 를 통해서 틀린 위치의 순서 파악하기
    count = 1
    for idx in range(len(words) - 1):
        # 앞 단어 끝 글자와 뒷 단어 첫 글자가 다를 경우,
        if words[idx][-1] != words[idx + 1][0]:
            count += 1
            
            if count % n == 0:
                answer[0] = n
                answer[1] = count // n
                break
                
            answer[0] = count % n
            answer[1] = (count // n) + 1
            break
            
        # 앞 단어 끝 글자와 뒷 단어 첫 글자가 같은 경우,
        elif words[idx][-1] == words[idx + 1][0]:
            count += 1
            
            if words[idx+1] in words[:idx+1]:
                if count % n == 0:
                    answer[0] = n
                    answer[1] = count // (n)
                    break
                answer[0] = (count) % n
                answer[1] = (count // n) + 1
                break
        
    
    
    # [방법1] math 를 사용한 방법
#     # 1. 리스트의 전체 길이로 진행
#     for i in range(len(words)-1):
#         # 2. 앞의 단어의 마지막 글자와 뒤의 단어의 첫 번째 글자가 같을 때,
#         if words[i][-1] == words[i+1][0]:
#             # 3. 만약, 뒤에 있는 단어가 그 전까지의 단어 중에서 있을 때 > 실패 
#             if words[i+1] in words[:i+1]:
#                 print(words[i+1])
#                 print(i+1)
#                 if (i+2) % n == 0:
#                     answer.append(n)
#                 else:
#                     answer.append((i+2) % n)
#                 answer.append(math.ceil((i+2) / n))
                
#         # 4. 앞의 단어의 마지막 글자와 뒤의 단어의 첫 번째 글자가 같지 않을 때, (완료)
#         elif words[i][-1] != words[i+1][0]:
#             answer_idx = words.index(words[i+1])
#             print(answer_idx+1)
#             if (answer_idx+1) % n == 0:
#                 answer.append(((answer_idx+1) % n) + n)
#             else:
#                 answer.append((answer_idx+1) % n)
#             answer.append(math.ceil((answer_idx+1) / n))
    
#     if answer == []:
#         answer.append(0)
#         answer.append(0)
    
    return answer