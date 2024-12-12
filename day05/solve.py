from ast import Tuple
import sys

with open(sys.argv[1], "r") as f:
    rulesets_str, pages_str = f.read().split("\n\n")

def task():
    result=0
    rules=[list(map(int, line.split('|'))) for line in rulesets_str.splitlines()]
    # for rule in sorted(rules):
    #     print(rule)
    for l in pages_str.splitlines():
        correct_list=True
        line=[int(x) for x in l.split(',')]
        # print(line)
        for prev in range(len(line)):
            for x in range(prev+1,len(line)):
                for rule in rules:
                    if rule[0]==line[x] and rule[1]==line[prev]:
                        correct_list=False
                        if not correct_list:
                            a=line[x]
                            line[x]=line[prev]
                            line[prev]=a
        # task1
        # if correct_list:
        #     result+=line[len(line)//2]
        # task2
        if not correct_list:
            result+=line[len(line)//2]
    print(result)
    
task()