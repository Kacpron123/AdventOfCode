import sys

matrix=[]
for line in iter(sys.stdin):
    matrix.append(line.strip())

def checkOutOfBounds(pos):
    return (pos[0] < 0 or pos[0] >= len(matrix[0]) or pos[1] < 0 or pos[1] >= len(matrix))
def symbol(pos):
    return matrix[pos[1]][pos[0]]
def moved(pos,dir):
    direction=[(0,-1),(1,0),(0,1),(-1,0)]
    return [pos[0]+direction[dir][0],pos[1]+direction[dir][1]]

memory={}
def PriceFence(position):
    flower=symbol(position)
    sameflower=[]
    border=[]
    if flower in memory:
        for areas in memory[flower]:
            if position in areas["places"]:
                return memory[flower]
    def check(pos):
        if pos not in sameflower:
            sameflower.append(pos)
            for i in range(4):
                movepos=moved(pos,i)
                if checkOutOfBounds(movepos) or symbol(movepos) != flower:
                    border.append([pos,movepos])
                elif symbol(movepos) == flower:
                    check(movepos)
    check(position)
    def CalculateSides():
        bordercopy=border.copy()
        result=0
        def next(side,mv,lenght):
            Direction=[(0,-1),(1,0),(0,1),(-1,0)]
            sideone,sidetwo=side
            return [[sideone[0]+Direction[mv][0]*lenght,sideone[1]+Direction[mv][1]*lenght] , [sidetwo[0]+Direction[mv][0]*lenght,sidetwo[1]+Direction[mv][1]*lenght]]
        for side in border:
            if side not in bordercopy:
                continue
            sideone,_=side
            for i in range(4):
                lenght=1
                nextside=next(side,i,lenght)
                while nextside in border:
                    bordercopy.remove(nextside)
                    lenght+=1
                    nextside=next(side,i,lenght)             
            if side in bordercopy:
                result+=1
                bordercopy.remove(side)
        return result
                
    temp={"places": sameflower,"area": len(sameflower),"border": len(border),"sides": CalculateSides()}
    if flower not in memory:
        memory[flower]=[temp]
    else:
        memory[flower].append(temp)
    # print("flower: ",flower," ",memory[flower,pos])
    return memory[flower]


for line in matrix:
    print(line)
print()
[PriceFence([x,y]) for x in range(len(matrix[0])) for y in range(len(matrix))]
result=0
result2=0
for x in memory:
    print(x)
    for area in memory[x]:
        print(area["area"],area["border"],area["sides"])
        result+=area["area"]*area["border"]
        result2+=area["area"]*area["sides"]
print("task1: ",result)
print("task2: ",result2)
# print("task1: ",[x['area'] for x in memory.items()] , [x['border'] for x in memory.items()])
