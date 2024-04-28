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
q = []
def compare(s,g):
    if s==g:
        return(1)
    else:
        return(0)
def find_pos(s):

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
                enqueue(new)

        new = down(curr_state,pos)
        if new != curr_state:
            if new == g:
                print ("found")
                return
            else:
                enqueue(new)
        new = right(curr_state,pos)
        if new != curr_state:
            if new == g:
                print ("Found")
                return
            else:
                enqueue(new)
        new = left(curr_state,pos)
        if new != curr_state:
            if new == g:
                
                print ("Found")
                return
            else:
                enqueue(new)
        print(new)
        if len(q) > 0:
            curr_state = dequeue()
            
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