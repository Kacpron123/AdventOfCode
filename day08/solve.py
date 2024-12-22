import sys
matrix=[]
for line in iter(sys.stdin):
    matrix.append(line.strip())
for line in matrix:
    print(line)
antennas={}
for y in range(len(matrix)):
    for x in range(len(matrix[0])):
        if matrix[y][x] != '.':
            if matrix[y][x] not in antennas.keys():
                antennas[matrix[y][x]]=[]
            antennas[matrix[y][x]].append([x,y])
def CheckOutOfRange(place):
    return 0 > place[0] or place[0] >= len(matrix[0]) or 0 > place[1] or place[1] >= len(matrix)
def antinodes(anten1,anten2):
    antinode=[]
    mv=[anten1[0]-anten2[0],anten1[1]-anten2[1]]
    antinode.append([anten1[0]+mv[0],anten1[1]+mv[1]])
    antinode.append([anten1[0]-2*mv[0],anten1[1]-2*mv[1]])
    return antinode
def antinodes2(anten1,anten2):
    antinode=[]
    mv=[anten1[0]-anten2[0],anten1[1]-anten2[1]]
    i=1
    while(True):
        place=[anten1[0]+i*mv[0],anten1[1]+i*mv[1]]
        if CheckOutOfRange(place):
            break
        antinode.append(place)
        i+=1
    i=-2
    while(True):
        place=[anten1[0]+i*mv[0],anten1[1]+i*mv[1]]
        if CheckOutOfRange(place):
            break
        antinode.append(place)
        i-=1
    return antinode
    
result=[]
# for task2:
for key,value in antennas.items():
    for antenna in value:
        result.append(antenna)
# -------------
for key in antennas.keys():
    print(key,':')
    for place in antennas[key]:
        # print(place)
        for place2 in antennas[key]:
            if place!=place2:
                # change here for two task
                # for x in antinodes(place,place2):
                for x in antinodes2(place,place2):
                    if x not in result and not CheckOutOfRange(x):
                        result.append(x)
                        matrix[x[1]]=matrix[x[1]][:x[0]]+'#'+matrix[x[1]][x[0]+1:]
                for line in matrix:
                    print(line)
                print()
print(len(result))