# # g = int(input())
# # p_1, p_2, p_3 = input().split()
# # if g == 1:
# #     print(print)
#
# def f(ham: str, eggs: str = 'eggs') -> str:
#      print("Annotations:", f.__annotations__)
#      print("Arguments:", ham, eggs)
#     return ham + ' and ' + eggs


#B096:爆弾の大爆発
#inpuarray

bomb = [[".",".","#","."],[".",".",".","."],[".","#",".","."],[".",".",".","."]]
print(len(bomb))
# bomb[0]= "#"
posi=[]
print(bomb[1][1])
for i in range(len(bomb)):
    for j in range(len(bomb[i])):
        if bomb[i][j] == "#":
            posi.append(i)
            posi.append(j)
        print(bomb[i][j],end=" ")
    print()

print(posi)

#bomb[posi[0]]
count = 0
for i in range(0, len(posi),2):
    for j in range(len(bomb[posi[0]])):
        bomb[posi[i]][j] = "x"
        count = count + 1

print(bomb)

for j in range(1, len(posi),2):
    for i in range(len(bomb[posi[0]])):
        bomb[i][posi[j]] = "x"
        count = count + 1

print(bomb,count)







