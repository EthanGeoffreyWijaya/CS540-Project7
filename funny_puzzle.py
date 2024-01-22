import heapq
import math


def get_manhattan_distance(from_state, to_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    distance = 0
    for i in range(9):
        if (from_state[i] == 0):
            continue
        x = abs((i % 3) - (to_state.index(from_state[i])) % 3)
        y = abs((int)(i / 3) - (int)(to_state.index(from_state[i])/ 3))
        distance += x + y
    return distance



def print_succ(state):
    succ_states = get_succ(state)

    for succ_state in succ_states:
        print(succ_state, "h={}".format(get_manhattan_distance(succ_state)))



def getNeighbors(index, state, states):
    if (index % 3 > 0 and state[index - 1] != 0):
        ts = state.copy()
        temp = ts[index - 1]
        ts[index - 1] = ts[index]
        ts[index] = temp
        states.append(ts)
    if(index % 3 < 2 and state[index + 1] != 0):
        ts = state.copy()
        temp = ts[index + 1]
        ts[index + 1] = ts[index]
        ts[index] = temp
        states.append(ts)
        
    if((int)(index / 3) > 0 and state[index - 3] != 0):
        ts = state.copy()
        temp = ts[index - 3]
        ts[index - 3] = ts[index]
        ts[index] = temp
        states.append(ts)
    if((int)(index / 3) < 2 and state[index + 3] != 0):
        ts = state.copy()
        temp = ts[index + 3]
        ts[index + 3] = ts[index]
        ts[index] = temp
        states.append(ts)



def get_succ(state):
    succ_states = []
    z1 = state.index(0)
    z2 = state.index(0, z1 + 1)
    getNeighbors(z1, state, succ_states)
    getNeighbors(z2, state, succ_states)
        
    return sorted(succ_states)




def solve(state, goal_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    maxlength = 0
    visited = [(get_manhattan_distance(state), state, (get_manhattan_distance(state), 0, -1))]
    pq = []
    path = []
    selected = (0,0,(0,0,-1))
    parent = 0
    #moves = 1
    while (state != goal_state):       
        neighbors = get_succ(state)
        for s in neighbors:
            if (s in (e[1] for e in visited)):
                continue
            g = get_manhattan_distance(s)
            heapq.heappush(pq, (g + visited[parent][2][1] + 1, 
                                s, (g, visited[parent][2][1] + 1, parent)))
        
        if (len(pq) == 0):
            return None
        #print(len(pq))
        if (len(pq) > maxlength):
            maxlength = len(pq)
        
        selected = heapq.heappop(pq)
        visited.append(selected)
        parent += 1
        #moves = selected[2][1] + 1
        state = selected[1]
        
    path.insert(0, selected)
    while (selected[2][2] != -1):
        selected = visited[selected[2][2]]
        path.insert(0, selected)
    for el in path:
        print((str)(el[1]) + " h=" + (str)(el[2][0]) + " moves: " + (str)(el[2][1]))
    
    print("Max queue length: " + (str)(maxlength))
    #print(*visited, sep="\n") 
    return path
    
"""
if __name__ == "__main__":
    #print_succ([3, 0, 6, 0, 4, 1, 7, 2, 5])
    #print()
    #print(get_manhattan_distance([2,5,1,4,3,6,7,0,0], [1, 2, 3, 4, 5, 6, 7, 0, 0]))
    #print()
    #solve([1,0,3,4,2,6,7,5,0])
    #solve([2,5,1,4,0,6,7,0,3])
    #print()
    solve([4,3,0,5,1,6,7,2,0])
    solve([3, 4, 6, 0, 0, 1, 7, 2, 5])
    solve([0, 4, 7, 1, 3, 0, 6, 2, 5])
    solve([1, 7, 0, 6, 3, 2, 0, 4, 5])
"""
