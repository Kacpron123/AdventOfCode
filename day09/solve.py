import sys

# take input
for line in iter(sys.stdin):
    input=line.strip()
    if len(input)%2==1:
        input+='0'
# print(input)
# making disc
numberId=0
disc=[]
for x1,x2 in zip(input[0::2],input[1::2]):
    disc+=[str(numberId) for _ in range(int(x1))]+['.' for _ in range(int(x2))]
    numberId+=1
# print(disc)

def task1():
    lhs=0
    rhs=len(disc)-1
    result=0
    while lhs<=rhs:
        # print(disc[lhs],disc[rhs])
        if disc[rhs]=='.':
            rhs-=1
            continue
        # print(disc[lhs] if disc[lhs] !='.' else disc[rhs], end="")
        if disc[lhs] == '.':
            result+=int(disc[rhs])*lhs
            rhs-=1
        else:
            result+=int(disc[lhs])*lhs
        lhs+=1
    print()
    print(result)

def task2():
    lhs,rhs=[0,len(disc)-1]
    lenspace,lenblock=[0,0]
    while 0<rhs:
        if disc[rhs] == '.':
            rhs-=1
            continue
        lenblock=rhs-(disc.index(disc[rhs],0,rhs) if disc[rhs] in disc[:rhs] else rhs)+1
        # lhs=0
        # print(lenblock)
        while lhs<rhs:
            # print(disc,"\n")
            if disc[lhs]=='.':
                lenspace+=1
            else:
                lenspace=0
            if lenspace>=lenblock:
                for i in range(lenblock):
                    disc[lhs-lenspace+1+i]=disc[rhs-i]
                    disc[rhs-i]='.'
                # print(''.join(disc),' ')
                break
            lhs+=1
        lenspace=0
        lhs=0
        rhs-=lenblock
        
    result=0
    for i in range(len(disc)):
        if disc[i]!='.':
            result+=int(disc[i])*i
    # print(''.join(disc))
    print(result)
# task1()
task2()