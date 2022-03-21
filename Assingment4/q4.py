#Beam Search Algorithm

def explore(graph,val,pq,parent,beta):
    if(graph[val]==None):
        return 
    for heu,name in graph[val]:
        node = (heu,val,name)
        pq.append(node)
        parent.append((val,name))     
    pq.sort()                          
    while(len(pq)>beta):
        pq.pop(beta)       

def get_steps(parent,goal):    
    node = goal             
    steps = []
    while(node!=None):
        steps.insert(0,node)    
        for p in parent:
            if(p[1]==node):
                node = p[0]    
                break
    return steps
def beam_search(graph,init,goal,beta):
    pq = [(None,None,init)]    
    parent=[(None,init)]      
    while(pq):                  
        val = pq.pop(0)[2]      
        if(val == goal):        
            steps = get_steps(parent,goal)
            return steps
        else:
            explore(graph,val,pq,parent,beta)   
    return None
if(__name__=='__main__'):
    graph = {
        'A' : [(1,'B'),(3,'C')],
        'B' : [(2,'D'),(2,'E')],
        'C' : [(3,'F'),(0,'G')],
        'D' : None,
        'E' : None,
        'F' : None,
        'G' : None,
    }
    init = 'A'
    goal = 'G'
    beta = 2
    steps = beam_search(graph,init,goal,beta)
    if(steps == None):
        print('\nBeam Search unsuccessful for beta:',beta)
    else:
        print('Steps:')
        print(steps)
    beta = 3
    steps = beam_search(graph,init,goal,beta)
    if(steps == None):
        print('\nBeam Search unsuccessful for beta:',beta)
    else:
        print('\nSteps for beta',beta,':')
        print(steps)