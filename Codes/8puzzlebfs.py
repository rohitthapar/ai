from math import sqrt
import sys
import copy
q = []
visited = []

def compare(a,b):
    if a==b:
        return 1
    else:
        return 0

def missingTile(currentState):
    for i in range(len(currentState)):
        for j in range(len(currentState[0])):
            if currentState[i][j] == 0:
                return ([i,j])

def up(currentState,position):
    row = position[0]
    col = position[1]
    s = copy.deepcopy(currentState)
    if row == 0:
        return (s)
    else:
        s[row][col],s[row-1][col] = s[row-1][col],s[row][col]
        return (s)


def down(currentState,position):
    row = position[0]
    col = position[1]
    s = copy.deepcopy(currentState)
    if row == len(s)-1:
        return (s)
    else:
        s[row][col], s[row + 1][col] = s[row + 1][col], s[row][col]
        return (s)

def left(currentState,position):
    row = position[0]
    col = position[1]
    s = copy.deepcopy(currentState)
    if col == 0:
        return (s)
    else:
        s[row][col], s[row][col-1] = s[row][col-1], s[row][col]
        return (s)

def right(currentState,position):
    row = position[0]
    col = position[1]
    s = copy.deepcopy(currentState)
    if col == len(s[0])-1:
        return (s)
    else:
        s[row][col], s[row][col+1] = s[row][col+1], s[row][col]
        return (s)

def enqueue(newState):
    if newState not in visited and newState not in q:
        q.append(newState)

def dequeue():
    global q
    if len(q) == 0:
        print("Goal state can't be achieved")
        sys.exit()
    else:
        x=q.pop(0)
        return x

def main():
    global q
    global visited
    initialState = [[2, 0, 3], [1, 8, 4], [7, 6, 5]]
    goalState = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    while(1):
        visited.append(initialState)
        position = missingTile(initialState)

        newState = up(initialState,position)
        if compare(newState,goalState) == 1:
            print(f'length is {len(visited)}')
            if compare(newState, goalState) == 1:
                print("Goal State achieved")
            sys.exit()
        enqueue(newState)

        newState = down(initialState, position)
        if compare(newState, goalState) == 1:
            print(f'length is {len(visited)}')
            if compare(newState, goalState) == 1:
                print("Goal State achieved")
            sys.exit()
        enqueue(newState)

        newState = left(initialState, position)
        if compare(newState, goalState) == 1:
            print(f'length is {len(visited)}')
            if compare(newState, goalState) == 1:
                print("Goal State achieved")
            sys.exit()
        enqueue(newState)

        newState = right(initialState, position)
        if compare(newState, goalState) == 1:
            print(f'length is {len(visited)}')
            if compare(newState, goalState) == 1:
                print("Goal State achieved")
            sys.exit()
        enqueue(newState)

        initialState = dequeue()



if __name__ == "__main__":
    main()
