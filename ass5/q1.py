 
def findfit(a , wt , val , fit , nonfit):
    maxwt=100
    for i in range(0 , len(a)):
        w =0
        v =0
        for  j in range(0, len(a[0])):
            if(a[i][j]):
                w=w+wt[j]
                v = v+val[j]
        
        if(w>100):
           
            nonfit.append((a[i] ,v))
           
        else:
            fit.append((a[i],v))

def crossover(a ,b):
    for i in range(2,4):
        temp=a[0][i]
        a[0][i]=b[0][i]
        b[0][i]=temp
def  mutatefirstchild(cycle , f):
    if(f[0][cycle]):
        f[0][cycle]=0
        return
    f[0][cycle]=1
def main():
    cycle =3
    a=[[1 ,1 ,1,1 ],[1 ,  0,0 ,0],[1 , 0 ,1 ,0], [1, 0,0,1]]
    for i in range(0,10):
        wt=[45 , 40 , 50 ,90]
        val=[3 ,5  ,8 ,10]
        fit=[]
        
        notfit=[]
    
        findfit(a, wt , val , fit , notfit)
        fit.sort(key = lambda x :x[1], reverse=True)
        notfit.sort(key = lambda x :x[1], reverse=True)
       
        final=fit+notfit
        crossover(final[2],final[3])
        mutatefirstchild(cycle , final[2])
        cycle-=1
        if(cycle==-1):
            cycle=3
        print(fit)
        print(final)
     
if __name__=='__main__':

    main()