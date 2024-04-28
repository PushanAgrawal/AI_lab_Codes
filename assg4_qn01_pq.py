# import copy

# def find_indices(arr, target):
#     for i, row in enumerate(arr):
#         for j, val in enumerate(row):
#             if val == target:
#                 return i, j
#     return None

# def swap(arr, row1, col1, row2, col2):
#     arr[row1][col1], arr[row2][col2] = arr[row2][col2], arr[row1][col1]

# def solve_8_puzzle(ini, fin, sol):
#     if ini == fin:
#         return sol
    
#     [i, j] = find_indices(ini, 0)  
#     print(ini)

#     if j < 2:
#         print(sol)
#         swap(ini, i, j, i, j + 1)
#         print(sol)
#         if ini not in sol:
#             sol.append(copy.deepcopy(ini))
#             return solve_8_puzzle(ini, fin, sol)
#         else:
#             swap(ini, i, j, i, j + 1)

#     if i < 2:
#         swap(ini, i, j, i + 1, j)

#         if ini not in sol:
#             sol.append(copy.deepcopy(ini))
#             return solve_8_puzzle(ini, fin, sol)
#         else:
#             swap(ini, i, j, i + 1, j)

#     if i > 0:
#         swap(ini, i, j, i - 1, j)
#         if ini not in sol:
#             sol.append(copy.deepcopy(ini))
#             return solve_8_puzzle(ini, fin, sol)
#         else:
#             swap(ini, i, j, i - 1, j)

#     if j > 0:
#         swap(ini, i, j, i, j - 1)
#         if ini not in sol:
#             sol.append(copy.deepcopy(ini))
#             return solve_8_puzzle(ini, fin, sol)
#         else:
#             swap(ini, i, j, i, j - 1)

# if __name__ == "__main__":
#     initial_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
#     final_state = [[2, 8, 1], [4, 0, 3], [7, 6, 5]]
    
#     sol = [initial_state]
#     solution = solve_8_puzzle(initial_state, final_state, sol.copy())
#     print(solution)
#     if solution:
#         print("Solution:")
#         for state in solution:
#             for row in state:
#                 print(row)
#             print()
#     else:
#         print("No solution found.")


import sys
import copy
from queue import PriorityQueue

class MaxPriorityQueue:
    def __init__(self):
        self.queue = PriorityQueue()

    def enqueue(self, priority, item):
        # Priority is negated to create a max priority queue
        self.queue.put((-priority, item))

    def dequeue(self):
        if not self.queue.empty():
            # Priority is negated again to retrieve the original priority
            return self.queue.get()[1]
        else:
            return None

    def peek(self):
        if not self.queue.empty():
            # Priority is negated again to retrieve the original priority
            return self.queue.queue[0][1]
        else:
            return None

    def size(self):
        return self.queue.qsize()
    
q = MaxPriorityQueue()
def ret_her(s,g):
    count=0
    i=0
    j=0
    for i in range(0,len(s)):
        for j in range(0, len(s[0])):
            if  s[i][j]!=g[i][j]:
                count+=1
    return count
def compare(s,g):
    if s==g:
        return(1)
    else:
        return(0)
def find_pos(s):
    print(s)
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == 0:
                return([i,j])
def up(s,pos):

 i = pos[0]
 j = pos[1]

 if i > 0:
    temp = copy.deepcopy(s)
    temp[i][j] = temp[i-1][j]
    temp[i-1][j] = 0
    return (temp)
 else:
    return (s)
def down(s,pos):
    i = pos[0]
    j = pos[1]

    if i < 2:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i+1][j]
        temp[i+1][j] = 0
        return (temp)
    else:
        return (s)
def right(s,pos):

 i = pos[0]
 j = pos[1]

 if j < 2:
    temp = copy.deepcopy(s)
    temp[i][j] = temp[i][j+1]
    temp[i][j+1] = 0
    return (temp)
 else:
    return (s)
def left(s,pos):

 i = pos[0]
 j = pos[1]

 if j > 0:
    temp = copy.deepcopy(s)
    temp[i][j] = temp[i][j-1]
    temp[i][j-1] = 0
    return (temp)
 else:
    return (s)
def enqueue(s):
    global q
    q = q + [s]
def dequeue():
    global q
 # find the state having minimum mis matches with the goal state
    elem = q[0]
    del q[0]
    return (elem)
def search(s,g):
    curr_state = copy.deepcopy(s)
    print(curr_state)
    curr_h=ret_her(s,g)
    if s == g:
        return
    c = 0
    while(1):

        pos = find_pos(curr_state)
        new = up(curr_state,pos)
       
        if new != curr_state:
            if new == g:
                print ("found")
                return
            else:
                val=ret_her(new,g)
                q.enqueue(val ,new)
        new = down(curr_state,pos)
        if new != curr_state:
            if new == g:
                print ("found")
                return
            else:
                val=ret_her(new,g)
                q.enqueue(val ,new)
        new = right(curr_state,pos)
        if new != curr_state:
            if new == g:
                print ("Found")
                return
            else:
                val=ret_her(new,g)
                q.enqueue(val ,new)
        new = left(curr_state,pos)
        if new != curr_state:
            if new == g:
                
                print ("Found")
                return
            else:
                val=ret_her(new,g)
                q.enqueue(val ,new)
        if q.size() > 0:
            curr_state = q.dequeue()
            
        else:
            print ("not found")
            return
def main():
    s = [[1,2,3],[8,0,4],[7,6,5]]
    g = [[2,8,1],[0,4,3],[7,6,5]]
    pos = find_pos(s)
    search(s,g)
if __name__ == "__main__":
     main()