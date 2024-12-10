import sys
import operator

from apport import Report

def iter_input():
    return (
        [int(x) for x in line.split(' ')] for line in iter(sys.stdin)
    )

def safe(report):
    if report[0]==report[1]:
        return False
    slope_rule=operator.gt if report[0]>report[1] else operator.lt
    prevX=report[0]
    for x in report[1:]:
        if not slope_rule(prevX,x):
            return False
        if not (1<= abs(prevX-x)<=3):
            return False
        prevX=x
    return True
def solve1():
    result=sum(map(safe,iter_input()))
    print(result)
def solve2():
    reports=tuple(iter_input())
    result=0
    for report in reports:
        for idx in range(len(report)):
            new_report=report[:idx]+report[idx+1:]
            if safe(new_report):
                result+=1
                break
    print(result)

#solve1()
solve2()