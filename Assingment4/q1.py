#Simple Hill Climbing +1/-1

from copy import deepcopy as dc

class pair:
    def __init__(self,below,block):
        self.below = below
        self.block = block


def heuristic(state,goal): 
    val = 0                 
    for ps in state:       
        for pg in goal:     
            if(ps.block == pg.block):
                if(ps.below == pg.below):  
                    val +=1
                else:
                    val -= 1              
                break
    return val

def get_top_blocks(state):         
    top = ['A','B','C','D']
    for pair in state:
        if pair.below in top:
            top.remove(pair.below)
    return top
def update(state,entry):  
    for p in state:
        if(p.block == entry.block):
            state.remove(p)
            state.append(entry)
            return

def move(init,goal):     
    state = dc(init)
    heu = heuristic(init,goal)
    top = get_top_blocks(state)
    for i in range(len(top)):
        for j in range(len(top)):   
            if( i == j ):  
                update(state,pair(None,top[i]))
                if(heuristic(state,goal)>heu):
                    return state
                state = dc(init)
            else:     
                update(state,pair(top[j],top[i]))
                if(heuristic(state,goal)>heu):
                    return state
                state = dc(init)
    return None   
def print_state(state):  
    for p in state:
        print((p.below,p.block),end=', ')
    print()
def solve(init,goal):  
    state = dc(init)
    while(state!=None):
        print_state(state)
        if(heuristic(state,goal)==len(state)):
            print('Hill Climb Successfull')
            print('Steps taken:',steps)
            return
        else:
            state = move(state,goal)
        steps +=1
    print('Hill Climb Unsuccessfull!')
    return
if(__name__=='__main__'):
    init = [pair(None,'B'),pair('B','C'),pair('C','D'),pair('D','A')]
    goal = [pair(None,'A'),pair('A','B'),pair('B','C'),pair('C','D')]
    solve(init,goal)