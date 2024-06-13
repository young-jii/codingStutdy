import sys

test_num = int(sys.stdin.readline().strip())
for i in range(test_num):
    test_li = sys.stdin.readline().strip().split()
    print(int(test_li[0]) + int(test_li[1]))