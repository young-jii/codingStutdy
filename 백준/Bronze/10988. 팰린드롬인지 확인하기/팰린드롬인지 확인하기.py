str_check = input()
mid_str = len(str_check) // 2
if len(str_check) % 2 == 1: 
    if str_check[:mid_str] == str_check[mid_str+1:][::-1]:
        print(1)
    else:
        print(0)
else:
    if str_check[:mid_str] == str_check[mid_str:][::-1]:
        print(1)
    else:
        print(0)