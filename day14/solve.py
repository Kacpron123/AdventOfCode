import sys

places,velocities=[],[]
def printMatrix(size):
    for y in range(size[1]):
        for x in range(size[0]):
            occurance=places.count([x,y])
            if occurance==0:
                print('.',end="")
            else:
                print(occurance,end="")
        print()
for line in iter(sys.stdin):
    l=line.split()
    p=l[0].split(',')
    p[0]=p[0].split('=')[1]
    v=l[1].split(',')
    v[0]=v[0].split('=')[1]
    places.append([int(x) for x in p])
    velocities.append([int(x) for x in v])
    # print(p,v)

def solve(size,seconds):
    for i in range(len(places)):
        x,y=places[i]
        vx,vy=velocities[i]
        places[i]=[(x+vx*seconds)%size[0],(y+vy*seconds)%size[1]]
def quadrant(size):
    midx=size[0]//2
    midy=size[1]//2
    quadrants=[0,0,0,0]
    for y in range(size[1]):
        for x in range(size[0]):
            if y<midy and x<midx:
                quadrants[0]+=places.count([x,y])
            elif y<midy and x>midx:
                quadrants[1]+=places.count([x,y])
            elif y>midy and x<midx:
                quadrants[2]+=places.count([x,y])
            elif y>midy and x>midx:
                quadrants[3]+=places.count([x,y])
    result=1
    for x in quadrants:
        result*=x 
    return result
print(places)
print(velocities)
# examplesize
# size=[11,7]
# inputsize
size=[101,103]
# solve(size,100)
# print(quadrant(size))
# printMatrix(size)
# -----------part two ---------
# i asume if some picture will show then shoud be some line so i will check if exist place in place[0] surrounding
def surrounding(pos):
    areaAxA=3
    midx=midy=areaAxA//2
    found=False
    for x in range(areaAxA):
        for y in range(areaAxA):
            if x!=y and places.count([pos[0]+x-midx,pos[1]+y-midy]) > 0:
                found=True
                break
        if found:
            break
    return found
from time import sleep
for i in range(50000):
    solve(size,1)
    if surrounding(places[0]) and surrounding(places[3]) and surrounding(places[6]) and surrounding(places[20]) and surrounding(places[26]):
        printMatrix(size)
        print()
        print(i+1)
        sleep(0.5)
# check until something show up on output and found it in 7383
print()
