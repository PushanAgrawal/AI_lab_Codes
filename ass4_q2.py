import copy
def find_pos(s):

    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == 0:
                return([i,j])
def hn(s,g):
     count=0
     for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] != g[i][j]:
                count+=1
     return count
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
 
def search(s,g):
   curr_state=copy.deepcopy(s)

   if s==g:
      return
   
   while(1):
        print(curr_state)
        pos=find_pos(curr_state)
        new = left(curr_state,pos)
        if new != curr_state:
        #    print(new)
        #    print(curr_state)
        #    print(hn(new,g))
        #    print(hn(curr_state,g))
           if s==g:   
              print("found")
           if(hn(new,g)<hn(curr_state,g)):
              print("hi")
              curr_state = new
              continue
        new = up(curr_state,pos)
        
        if new != curr_state:
            if s==g:   
              print("found")
            if(hn(new,g)<hn(curr_state,g)):
              curr_state = right(curr_state,pos)
              print(curr_state)
              continue

          
           
      
        
        new = right(curr_state,pos)
        
        if new != curr_state:
            if curr_state==g:   
              print("found")
              return
            if(hn(new,g)<hn(curr_state,g)):
              curr_state = right(curr_state,pos)
              print(curr_state)
              continue
        new = down(curr_state,pos)
        if new != curr_state:
           if curr_state==g:   
              print("found")
              return
           if(hn(new,g)<hn(curr_state,g)):
              curr_state = new
              continue
        print("not found")
        break
          
            
        
   


def main():
    s = [[2,0,3],[1,8,4],[7,6,5]]
    g = [[1,2,3],[8,0,4],[7,6,5]]
 
    
    search(s,g)

 
if __name__ == '__main__':
   main()
