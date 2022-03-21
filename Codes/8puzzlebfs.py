import sys
import copy

initialState = [[1,2,3],[8,0,4],[7,6,5]]
goalState = [[2,8,1],[0,4,3],[7,6,5]]

q = []
visited_q = []
def compare(currentState,goalState):
    val = False
    for i in range(3):
        for j in range(3):
            if currentState[i][j] == goalState[i][j]:
                val = True
            else:
                val = False
    return val

def findPosition(currentState):
    for i in range(len(currentState)):
        for j in range(len(currentState[0])):
            if(currentState[i][j] == 0):
                return([i,j])

# up down left rigth -> function define
# enqueue dequeue
#
