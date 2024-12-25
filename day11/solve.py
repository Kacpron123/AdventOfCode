from re import I
import sys

stones = [int(y) for x in sys.stdin for y in x.split()]

memory={}
def solve(stone,blink):
    if blink==0:
        return 1
    elif (stone,blink) in memory:
        return memory[(stone,blink)]
    elif stone==0:
        val = solve(1,blink-1)
    elif len(str(stone))%2==0:
        strstone=str(stone)
        mid=len(strstone)//2
        left=stone//(10**mid)
        right=stone%(10**mid)
        val=solve(left,blink-1)+solve(right,blink-1)
    else:
        val=solve(stone*2024,blink-1)
    memory[(stone,blink)]=val
    return val

print(sum(solve(stone,25) for stone in stones))
print(sum(solve(stone,75) for stone in stones))