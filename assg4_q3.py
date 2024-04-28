import copy
class PriorityQueue(object):
    def __init__(self):
        self.queue = []
        self.closed=[]
 
    # def __str__(self):
    #     return ' '.join([str(i) for i in self.queue])
 
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
 
    # for inserting an element in the queue
    def insert(self, data):
        check=False
        for i in self.queue:
            if i[0]==data[0]:
                check=True
                if i[1]+i[2]>data[1]+data[2]:
                    i[1]=data[1]
                    i[2]=data[2]
                    return
        
        if(check):
            return
        if data[0] in self.closed :
            return

        self.queue.append(data)
 
    # for popping an element based on Priority
    def delete(self):
        try:
            max_val = 0
            for i in range(len(self.queue)):
                if self.queue[i][1] >= self.queue[max_val][1]:
                    max_val = i
            item = self.queue[max_val]
            self.closed.append(item[0])
            del self.queue[max_val]
            return item
        except IndexError:
            print()
            exit()


q=PriorityQueue()
def find_pos(s):

    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == 0:
                return([i,j])
def hn(s,g):
     count=0
     for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == g[i][j]:
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
    if s == g:
        return
    count=1
    
    while(1):

        pos=find_pos(curr_state)
        new = right(curr_state,pos)
        if new != curr_state:
            q.insert((new,hn(new,g),count))
  
        new = down(curr_state,pos)
        if new != curr_state:
            
            q.insert((new,hn(new,g),count))
        new = left(curr_state,pos)
        if new != curr_state:

          q.insert((new,hn(new,g),count))
        new = right(curr_state,pos)
        if new != curr_state:
            q.insert((new,hn(new,g),count))
      
        if (~(q.isEmpty())):
            print(q.queue)
            (curr_state,h,gn) = q.delete()
            print(curr_state)
            print(h+gn)
          
            
            if(curr_state==g):
                print("found")
                return
            
        else:
            print ("not found")
            return
        count+=1
        print(count)


def main():
    s = [[2,0,3],[1,8,4],[7,6,5]]
    g = [[1,2,3],[8,0,4],[7,6,5]]
    # q.insert((s,hn(s,g),0))
    
    search(s,g)

 
if __name__ == '__main__':
    myQueue = PriorityQueue()
    # myQueue.insert((12,[]))
    # myQueue.insert((1,[]))
    # myQueue.insert((3,[]))
    # myQueue.insert((2,[]))
    print("great")
    main()