import random
import math

def eq_val(arr):
    ans= (((~arr[0])|arr[1])&((~arr[2])|(~arr[3]))&(arr[2]|arr[3])&((~arr[1])|(~arr[3]))&((~arr[0])|(~arr[3])))
    return ans

def hn(arr):
    ans=0
    if((not arr[0])or arr[1]):
        ans+=1
    if(not(arr[2]) or not arr[3] ):
        
        ans+=1
    if(arr[2]or arr[3]):
        ans+=1
    if((not[1])or (not arr[3])):
        ans+=1
    if((not arr[1])|(not arr[3])):
        ans+=1
    return ans
def val(e , t ):
    return  (1/(1+(math.exp(-e/t))))

def main():
    ini=[1,1,1,1]
    delt=50
    if(eq_val(ini)):
        return ini
    heruold=hn(ini)
    t=500
    random_num=[0.655,0.254,0.432]
    while(1):
        ini=[random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)]
        print(ini)
        print(hn(ini))
        if(eq_val(ini)):
            return ini
        herunew=hn(ini)
       
        if((herunew-heruold)>=0):
            t=t-delt
            heruold=hn(ini)
            continue
        val1=val(herunew-heruold, t)
        if(val1>0.5):
            heruold=herunew
            t=t-delt
            
        elif(random_num[random.randint(0,2)]<val1):
            heruold=herunew
            t=t-delt
            print(ini)
    

        

    

if __name__ =="__main__":
    print(main())