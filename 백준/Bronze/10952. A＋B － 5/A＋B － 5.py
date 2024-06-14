while(True):
    test_li = input().split(' ')
    if test_li[0] == '0' and test_li[1] == '0':
        break
    else:
        print(int(test_li[0])+int(test_li[1]))