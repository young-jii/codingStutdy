num_li = []
for i in range(9):
    num_li.append(int(input()))

max_num = max(num_li)
print(max_num)
print(num_li.index(max_num)+1)