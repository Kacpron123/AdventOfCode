import sys
#movement up,right,down,left
matrix=[]
for line in iter(sys.stdin):
    matrix.append(line.strip())
    print(line)
    pilot=[]
    for idy in range(len(matrix)):
        for idx in range(len(matrix[0])):
            if matrix[idy][idx]=='^':
                pilot=[idx,idy]
                break
        if pilot:
            break
def PlaceSymbol(matrix,pilot,symbol):
    matrix[pilot[1]]=matrix[pilot[1]][:pilot[0]] + symbol + matrix[pilot[1]][pilot[0]+1:]
def isBorder(matrix,pilot):
    return (0 < pilot[0] < len(matrix[0])-1) and (0 < pilot[1] < len(matrix)-1)
def move(pilot,movement):
    Direction = [[0 , -1],[1 , 0],[ 0, 1],[-1 , 0]]
    pilot[0]+=Direction[movement][0]
    pilot[1]+=Direction[movement][1]
    return pilot
def matrixSymbol(matrix,pilot):
    if not isBorder:
        return -1
    return matrix[pilot[1]][pilot[0]]
def checkOutOfBounds(pos):
    return (pos[0] < 0 or pos[0] >= len(matrix[0]) or pos[1] < 0 or pos[1] >= len(matrix))

def task1():
    movement=0
    pilot=[]
    for idy in range(len(matrix)):
        for idx in range(len(matrix[0])):
            if matrix[idy][idx]=='^':
                pilot=[idx,idy]
                break
        if pilot:
            break
    result=0
    while  isBorder(matrix,pilot):
        PlaceSymbol(matrix,pilot,'X')
        move(pilot,movement)
        # print(pilot)
        if matrixSymbol(matrix,pilot)=='#':
            move(pilot,(movement+2)%4)
            # change direction clockwise
            movement=(movement+1)%4
    PlaceSymbol(matrix,pilot,'X')
    for row in matrix:
        for x in row:
            if x == 'X':
                result+=1
    print(result)

from time import sleep
def checkloop(start,movement,placed):
    trace=list()
    LoopPilot=start.copy()
    PlaceSymbol(matrix,placed,'O')
    while(True):
        Loopnextpos=move(LoopPilot.copy(),movement)
        if checkOutOfBounds(Loopnextpos):
            return False
        if  matrixSymbol(matrix,Loopnextpos) =='#' or Loopnextpos==placed:
            movement=(movement+1)%4
            continue
        if list(LoopPilot)+[movement] in trace:
            for line in matrix:
                print(line)
            print()
            return True
        trace.append(list(LoopPilot)+[movement])
        move(LoopPilot,movement)
    return False
def task2():
    
    movement=0
    result=0
    PlaceSymbol(matrix,pilot,'X')
    while(True):
        # sleep(0.3)
        # PlaceSymbol(matrix,pilot,'1')
        # for line in matrix:
        #     print(line)
        # print()
        nextpos=move(pilot.copy(),movement)
        if checkOutOfBounds(nextpos):
            break
        # print(pilot)
        if matrixSymbol(matrix,nextpos)=='#':
            movement=(movement+1)%4
            continue
        # checking for loop
        if matrixSymbol(matrix,nextpos) != 'X':
            if checkloop(pilot.copy(),movement,nextpos):
                result+=1
                print(result)
        move(pilot,movement)
        PlaceSymbol(matrix,pilot,'X')
        
    print(result)

# task1()
task2() 