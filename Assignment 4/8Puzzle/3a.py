from math import sqrt
def missing_tile(currentState):
    for i in range(3):
        for j in range(3):
            if currentState[i][j] == 0:
                return ([i,j])

def euclidean(x1,y1,x2,y2):
    euc = sqrt(pow(x2-x1,2)+pow(y2-y1,2))
    return euc

def manhattan(x1,y1,x2,y2):
    man = abs(x2-x1) + abs(y2-y1)
    return man

def minkowski(x1,x2,y1,y2,p):
    mink = pow(pow(x2-x1,p)+pow(y2-y1,p),1/p)
    return mink

def main():
    istate = [[2,0,3],[1,8,4],[7,6,5]]
    fstate = [[1,2,3],[8,0,4],[7,6,5]]
    p = int(input('Enter value of P', ))
    x1,y1 = missing_tile(istate)
    x2,y2 = missing_tile(fstate)
    euc = euclidean(x1,y1,x2,y2)
    print(f'Euclidean Distance is {euc}')
    man = manhattan(x1, y1, x2, y2)
    print(f'Manhattan Distance is {man}')
    mink = minkowski(x1, y1, x2, y2,p)
    print(f'Minkowski Distance is {mink}')

if __name__ == "__main__":
    main()