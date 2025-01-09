import sys

from sympy import Symbol

warehouse=[]
moves=''
pilot=[]
def getinput(part: int):
    global moves,pilot,warehouse
    Checkmoves=False
    for line in iter(sys.stdin):
        if line=='\n':
            Checkmoves=True
            continue
        if not Checkmoves:
            line=line.splitlines()
            if '@' in line[0]:
                pilot=[line[0].index('@'),len(warehouse)]
            warehouse.append(''.join(line))
        else:
            moves+=line.replace('\n','')
    if part==2:
        warehouse=[''.join(['..' if x=='.' else '@.' if x=='@' else '[]' if x=='O' else '##' for x in line]) for line in warehouse]
        pilot[0]*=2
def move(pos,mv):
    Direction=[(0,-1),(1,0),(0,1),(-1,0)] #up,right,down,left
    return [pos[0]+Direction[mv][0],pos[1]+Direction[mv][1]]
def symbol(pos):
    return warehouse[pos[1]][pos[0]]
def SymbolPlace(pos,symbol: str):
    warehouse[pos[1]]=warehouse[pos[1]][:pos[0]]+symbol+warehouse[pos[1]][pos[0]+1:]
def CanMoveBox(pos,mv):
    nextpose=move(pos,mv)
    if symbol(pos)=='.':
        return True
    elif symbol(pos)=='O':
        return CanMoveBox(nextpose,mv)
    elif symbol(pos) in ['[',']']:
        # horizontal
        if mv%2==1:
            return CanMoveBox(move(nextpose,mv),mv)
        else:
            otherhalfpos=move(pos,1) if symbol(pos)=='[' else move(pos,3)
            othernextpose=move(otherhalfpos,mv)
            return CanMoveBox(nextpose,mv) and CanMoveBox(othernextpose,mv)

    else:
        return False
    
def moveBiggerBox(nextpos):
    print()
def solve(part: int):
    def cost():
        result=0 
        for y in range(len(warehouse)):
            for x in range(len(warehouse[0])):
                if symbol([x,y]) in ['O','[']:
                    result+=x+100*y
        print(result)
    global pilot
    for x in moves:
        # for line in warehouse:
        #     print(line)
        # print(x)
        mv=0 if x=='^' else 1 if x=='>' else 2 if x=='v' else 3
        nextpos=move(pilot,mv)
        if symbol(nextpos)=='.':
            SymbolPlace(pilot,'.')
            SymbolPlace(nextpos,'@')
            pilot=nextpos
            continue
        if symbol(nextpos)=='O' and CanMoveBox(nextpos,mv):
            SymbolPlace(pilot,'.')
            pilot=nextpos
            SymbolPlace(pilot,'@')
            nextpos=move(nextpos,mv)
            while symbol(nextpos) == 'O':
                SymbolPlace(nextpos,'O')
                nextpos=move(nextpos,mv)
            SymbolPlace(nextpos,'O')
            continue
        elif symbol(nextpos) in ['[',']'] and CanMoveBox(nextpos,mv):
            if mv%2==1:
                prev=symbol(pilot)
                SymbolPlace(pilot,'.')
                pilot=nextpos
                while symbol(nextpos) != '.':
                    s=prev
                    prev=symbol(nextpos)
                    SymbolPlace(nextpos,s)
                    nextpos=move(nextpos,mv)
                SymbolPlace(nextpos,prev)
            else:
                def MoveBlocks(s,nextpos,mv):
                    if symbol(nextpos) == '.':
                        SymbolPlace(nextpos,s)
                        return 1
                    otherpos=move(nextpos,1) if symbol(nextpos) == '[' else move(nextpos,3)
                    prev=symbol(nextpos)
                    otherprev=symbol(otherpos)
                    SymbolPlace(nextpos,s)
                    MoveBlocks(prev,move(nextpos,mv),mv)
                    SymbolPlace(otherpos,'.')
                    MoveBlocks(otherprev,move(otherpos,mv),mv)

                prev=symbol(pilot)
                SymbolPlace(pilot,'.')
                pilot=nextpos
                MoveBlocks('@',nextpos,mv)

                


    cost()

part=2
getinput(part)
for line in warehouse:
    print(line)
print(moves)
print(pilot)
solve(part)
for line in warehouse:
    print(line)