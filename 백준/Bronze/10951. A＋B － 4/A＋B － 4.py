while True:
    try :
        test_li = input().split(' ')
        print(int(test_li[0])+int(test_li[1]))
    except EOFError:
        break