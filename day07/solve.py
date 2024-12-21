import sys
from itertools import product

input=[]
for line in iter(sys.stdin):
    sum, numbers = line.split(':')
    input.append((int(sum),[int(x) for x in numbers.split()]))
    # input.append([sum,numbers])
def task1():
    result=00
    for line in input:
        numbersum=0
        for oper in list(product(['+','*'],repeat=len(line[1])-1)):
            numbersum=line[1][0]
            for x in range(len(line[1])-1):
                if oper[x] == '+':
                    numbersum+=line[1][x+1]
                if oper[x] == '*':
                    numbersum*=line[1][x+1]
                if numbersum >= line[0]:
                    break
            other=[f"{oper[g]}{line[1][g+1]}" for g in range(len(line[1])-1)]
            print(str(line[1][0])+"".join(other)+'='+str(numbersum) + ' vs '+str(line[0]))
            if numbersum == line[0]:
                result+=line[0]
                print(line[0])
                break
        print()
    print(result)

def task2():
    result=0
    for line in input:
        numbersum=0
        for oper in list(product(['+','*','||'],repeat=len(line[1])-1)):
            numbersum=line[1][0]
            for x in range(len(line[1])-1):
                num=line[1][x+1]
                if oper[x] == '+':
                    numbersum+=num
                if oper[x] == '*':
                    numbersum*=num
                if oper[x] == '||':
                    numbersum=int(str(numbersum)+str(num))
                if numbersum > line[0]:
                    break
            if numbersum == line[0]:
                other=[f"{oper[g]}{line[1][g+1]}" for g in range(len(line[1])-1)]
                # print(str(line[1][0])+"".join(other)+'='+str(numbersum) + ' vs '+str(line[0]))
                result+=line[0]
                break
    print(result)
        
# task1()
task2()