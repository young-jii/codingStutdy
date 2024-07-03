naLi = []
for i in range(10):
    num = int(input())
    naLi.append(num%42)

print(len(set(naLi)))