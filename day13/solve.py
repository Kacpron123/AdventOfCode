import sys
lines = iter(sys.stdin)

def solve(part: int):
    result=0
    add = 10000000000000 if part==2 else 0
    for line in lines:
        if line.startswith("Button"):
            l=line.split(" ")
            button=l[1][0]
            if button=='A':
                Ax=int(l[2][1:-1])
                Ay=int(l[3][1:-1])
                print(Ax,Ay)
            else:
                Bx=int(l[2][1:-1])
                By=int(l[3][1:-1])
                print(Bx,By)
        elif line.startswith("Prize:"):
            l=line.split(" ")
            Px=int(l[1][2:-1])+add
            Py=int(l[2][2:-1])+add
            detAB=Ax*By-Ay*Bx
            x=(By*Px-Bx*Py)/detAB
            y=(-Ay*Px+Ax*Py)/detAB
            print(Px,Py)
            
            if x%1==0 and y%1==0:
                print("res: ",3*x,y,'=',3*x+y)
                result+=3*x+y
            
        else:
            print()
    print(result)
                

# solve(1)
solve(2)