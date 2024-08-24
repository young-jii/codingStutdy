letter = input()

check_let = letter.upper()
# print(check_let)
alpha_dic = {"A":0, "B":0, "C":0, "D":0, "E":0, "F":0, "G":0, 
             "H":0, "I":0, "J":0, "K":0, "L":0, "N":0, "M":0, "O":0, "P":0, 
             "Q":0, "R":0, "S":0, "T":0, "U":0, "V":0, "W":0, "X":0, "Y":0, "Z":0}
# print(alpha_dic.keys())
for i in check_let:
    if i in alpha_dic.keys():
        alpha_dic[i] += 1

# print(alpha_dic)

answer = [k for k, v in alpha_dic.items() if v == max(alpha_dic.values())]

if len(answer) >= 2 :
    print("?")
else:
    print(answer[0])