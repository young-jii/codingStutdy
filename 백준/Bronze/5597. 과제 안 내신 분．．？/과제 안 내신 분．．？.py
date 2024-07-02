cnt = 0
num_li = []

while True:
    num = int(input())
    num_li.append(num)
    cnt += 1
    if cnt == 28:
        break

for i in range(1, 31, 1):
    if i not in num_li:
        print(i)