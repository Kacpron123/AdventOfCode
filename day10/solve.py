import sys

matrix=[]
for line in iter(sys.stdin):
    matrix.append(line.strip())
def CheckOutOfBonds(pilot):
    return 0>pilot[0] or pilot[0]>=len(matrix[0]) or 0>pilot[1] or pilot[1]>=len(matrix)
direction=[(0,-1),(1,0),(0,1),(-1,0)]
def moved(pilot,direct):
    return [pilot[0]+direction[direct][0],pilot[1]+direction[direct][1]]
def symbol(pilot):
    return matrix[pilot[1]][pilot[0]]

collected=[]
result2=0
def GoUp(pilot):
    global result2
    # print(pilot,'=',symbol(pilot))
    if symbol(pilot) == '9':
        result2+=1
        if pilot not in collected:
            # print("found")
            collected.append(pilot)
    for i in range(4):
        movedpilot=moved(pilot,i)
        if not CheckOutOfBonds(movedpilot) and int(symbol(pilot))+1 == int(symbol(movedpilot)):
            GoUp(movedpilot)
    return len(collected)

for line in matrix:
    print(line)

result=0
prevresult=0
for y in range(len(matrix)):
    for x in range(len(matrix[0])):
        if matrix[y][x] == '0':
            result+=GoUp([x,y])
            collected=[]

print()
print(result)
print(result2)