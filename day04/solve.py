import sys

XMAS='XMAS'
XMAS_R='SAMX'
def occurances(string,sub):
    count=start=0
    while True:
        start=string.find(sub,start)+1
        if start > 0:
            count+=1
        else:
            return count

def diagonals_right(matrix):
    row=len(matrix)
    col=len(matrix[0])
    diagonals=[]
    for start in range(col):
        x,y=start,0
        diagonal=[]
        while x<col and y<row:
            diagonal.append(matrix[y][x])
            x+=1
            y+=1
        diagonals.append(''.join(diagonal))
    for start in range(col)[1:]:
        diagonal=[]
        x,y=0,start
        while x<col and y<row:
            diagonal.append(matrix[y][x])
            x+=1
            y+=1
        diagonals.append(''.join(diagonal))
    return diagonals
def diagonals_left(matrix):
    return diagonals_right(matrix[::-1])



matrix=tuple(sys.stdin.read().splitlines())
def task1():
    result=0
    result+=sum(occurances(line,XMAS)+occurances(line,XMAS_R) for line in matrix)
    result+=sum(occurances(line,XMAS)+occurances(line,XMAS_R) for line in diagonals_left(matrix))
    result+=sum(occurances(line,XMAS)+occurances(line,XMAS_R) for line in diagonals_right(matrix))
    result+=sum(occurances(line,XMAS)+occurances(line,XMAS_R) for line in [''.join(row[col] for row in matrix) for col in range(len(matrix))])
    print(result)

def task2():
    result=0
    for idy in range(1,len(matrix)-1):
        for idx in range(1,len(matrix[0])-1):
            if matrix[idy][idx] == 'A':
                if ((matrix[idy-1][idx-1]=='M' and matrix[idy+1][idx+1]=='S' 
                    or matrix[idy-1][idx-1]=='S' and matrix[idy+1][idx+1]=='M')
                    and (matrix[idy-1][idx+1]=='M' and matrix[idy+1][idx-1]=='S'
                    or matrix[idy-1][idx+1]=='S' and matrix[idy+1][idx-1]=='M')):
                    result+=1
    print(result)


# task1()
task2()