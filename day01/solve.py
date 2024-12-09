import sys
import bisect

left,right=[],[]

def solve1():
    for line in iter(sys.stdin):
        a,b=map(int,line.split('  '))
        bisect.insort(left,a)
        bisect.insort(right,b)
    print("rozwiazanie1: ","")
    print(sum(abs(x-y) for x,y in zip(left,right)))

def solve2():
    for line in iter(sys.stdin):
        a,b=map(int,line.split('  '))
        left.append(a)
        right.append(b)
    print(sum(x*right.count(x) for x in left))

solve1()
solve2()