list=[1,5,6,3,6,0]
print(list)

for x in range(len(list)-1,-1,-1):
    print(list[x])

list.append(239)
list.insert(2, 9)

print(list)

twodlist=[[1,2,5,6],
          [3,4,7,8],
          [9,27]]

print(twodlist[2][1])
print('Rows: ', len(twodlist))
print('Columns:', len(twodlist[0]))

for x in range(0,len(twodlist)):
    for y in range(0,len(twodlist[x])):
        print(twodlist[x][y])

"""row= int(input("How many rows would you like? "))
column = int(input("How many columns would you like? "))

list2d=[]
for x in range(0,row):
    list2d.append([])
    for y in range(0,column):

        list2d[x].append(input('Enter value: '))

print(list2d)

for x in range(0,len(list2d)):
    print(list2d[x][x])

count=0

for counter in range(len(list2d)-1, -1, -1):
    print(list2d[counter][count]) 
    count+=1

"""

square = [[1,2,3],
          [4,5,6],
          [7,8,9]
          ]

square2 = [[11,21,31],
          [41,51,61],
          [71,81,91]
          ]

squareadd=[]

for x in range(0,len(square)):
    squareadd.append([])
    for y in range(0,len(square[x])):
        squareadd[x].append(square[x][y]+square2[x][y])
    #print(squareadd)


print(squareadd)

squaremult=[]

for x in range(0,len(square)):
    squaremult.append([])
    for y in range(0,len(square[x])):
        squaremult[x].append(square[x][y]*square2[x][y])
   # print(squaremult)


print(squaremult)

for x in range(len(squaremult)-1, -1,-1):
    for y in range(len(squaremult[x])-1,-1,-1):
        print(squaremult[x][y])