# # g = int(input())
# # p_1, p_2, p_3 = input().split()
# # if g == 1:
# #     print(print)
#
# def f(ham: str, eggs: str = 'eggs') -> str:
#      print("Annotations:", f.__annotations__)
#      print("Arguments:", ham, eggs)
#     return ham + ' and ' + eggs
'''
4 3
. . .
# . .
. . .
. . .
'''

#B096:爆弾の大爆発
#inpuarray

#bomb = [["#",".",".","."],[".",".",".","."],[".",".",".","."],[".",".",".","."]]
h,w=input().split()
bomb=[]
for i in range(int(h)):
    vec=[]
    myStr=input()
    for j in range(int(w)):
        vec.append(myStr[j])
    bomb.append(vec)

# print(len(bomb))
# bomb[0]= "#"
posi=[]
#print(bomb[1][1])
def find_char(myChar):
    kount=0
    for i in range(len(bomb)):
        for j in range(len(bomb[i])):
            if bomb[i][j] == myChar:
                posi.append(i)
                posi.append(j)
                kount = kount +1
    return kount
x=find_char("#")
# print("# count",x)
# print("# positon",posi)

#bomb[posi[0]]
count = 0
for i in range(0, len(posi),2):
    for j in range(int(w)):
        bomb[posi[i]][j] = "x"

# print(bomb)

for j in range(1, len(posi),2):
    for i in range(int(h)):
        bomb[i][posi[j]] = "x"

# print(bomb)
x= find_char("x")
print(x)




